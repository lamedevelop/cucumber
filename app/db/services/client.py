from app.db.models.client import Client
from app.db.schema import clients_table
from app.db.services.abstract import AbstractService


class ClientService(AbstractService):

    async def get_client(self, client_id: int):
        row = await self.select(
            clients_table.select().where(
                clients_table.c.client_id == client_id,
            )
        )
        return Client(**row) if row else False