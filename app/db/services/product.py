from app.db.models.product import Product
from app.db.schema import products_table
from app.db.services.abstract import AbstractService


class ProductService(AbstractService):

    async def get_products(self, args: dict = None):
        args = await self.prepare_args(args)
        session = await self.get_session()

        rows = session.query(products_table) \
            .filter_by(**args) \
            .all()

        return [Product(**row) for row in rows]

    async def get_product(self, product_id: int):
        row = await self.select(
            products_table.select().where(
                products_table.c.product_id == product_id,
            )
        )
        return Product(**row) if row else False
