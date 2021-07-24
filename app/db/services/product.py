from app.db.services.abstract import AbstractService
from app.db.models.product import Product, Category
from app.db.schema import products_table, categories_table


class ProductService(AbstractService):

    async def get_products(self, args: dict = None):
        rows = await self.select_multi(products_table, args)
        return [Product(**row) for row in rows]

    async def get_categories(self, args: dict = None):
        rows = await self.select_multi(categories_table, args)
        return [Category(**row) for row in rows]

    async def get_product(self, product_id: int):
        row = await self.execute(
            products_table.select().where(
                products_table.c.product_id == product_id,
            )
        )
        return Product(**row) if row else False
