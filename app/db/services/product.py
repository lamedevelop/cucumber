from app.db.models.product import Product
from app.db.schema import products_table
from app.db.services.abstract import AbstractService


class ProductService(AbstractService):

    async def get_products(self):
        res = []

        session = await self.get_session()
        rows = session.query(products_table) \
            .filter(products_table.c.category.in_([1])) \
            .all()

        for row in rows:
            res.append(Product(**row))

        return res
