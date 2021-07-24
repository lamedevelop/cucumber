from app.db.services.abstract import AbstractService
from app.db.models.product import Product, Category
from app.db.schema import clients_table


class ClientService(AbstractService):

    async def get_client(self, client_id: int):
        row = await self.select(
            clients_table.select().where(
                clients_table.c.client_id == client_id,
            )
        )
        return Product(**row) if row else False
