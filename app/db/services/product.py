from app.db.schema import products_table
from app.db.services.abstract import AbstractService


class Args:
    pass


class ProductService(AbstractService):

    async def get_products(self):
        session = await self.get_session()
        row = session.query(products_table) \
            .filter(products_table.c.category.in_([1])) \
            .all()

        if row:
            print(row)
            return row
        else:
            return False
