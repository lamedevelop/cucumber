from app.db.services.validation import ValidationService
from app.internal.file_manager import FileManager
from app.db.services.abstract import AbstractService
from app.db.schema import clients_table
from app.db.models.client import Client, ClientInRequest


class ClientService(AbstractService):

    image_template = 'client_%s.jpg'

    async def register_client(self, client: dict):
        client = ClientInRequest(**client)
        client_id = await self.add_client(client)
        if client_id:
            await ValidationService().send_validation(
                Client(
                    client_id=client_id,
                    **client.dict()
                )
            )
            return client_id
        else:
            return False

    async def add_client(self, client: ClientInRequest):
        client_id = await self.execute(
            clients_table.insert().values({
                **client.dict()
            }).returning(clients_table.c.client_id)
        )
        return client_id[0] if client_id else False

    async def update_client(self, client_id: int, update_fields: dict):
        if not await self.get_client(client_id):
            return False

        client_row = await self.execute(
            clients_table.update()
            .where(clients_table.c.client_id == client_id)
            .values(**update_fields)
            .returning("*")
        )

        return Client(**client_row) if client_row else False

    async def get_client(self, client_id: int):
        row = await self.execute(
            clients_table.select().where(
                clients_table.c.client_id == client_id,
            )
        )
        return Client(**row) if row else False

    async def get_client_image_filename(self, client_id: int):
        filename = FileManager.media_files_dir + self.image_template % client_id
        return filename if FileManager.is_file(filename) else False
