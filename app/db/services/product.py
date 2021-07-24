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
