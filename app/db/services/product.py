# TODO: make products service
from app.db.pool_manager import PoolManager
from app.db.schema import products_table


class Args:
    pass


class AbstractService(object):
    pass


class ProductService(AbstractService):

    async def get_products(self):
        row = await PoolManager().execute(products_table.select().where(
            products_table.c.category == 1
        ))

        if row:
            print(row)
            return row
        else:
            return False
