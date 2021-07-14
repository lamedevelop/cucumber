from sqlalchemy import and_

from app.db.schema import products_table
from aiopg.sa import create_engine

from app.db.settings import DbSettings


class Args:
    pass


class AbstractService(object):

    async def execute(self, query):
        async with create_engine(DbSettings.dsn()) as engine:
            async with engine.acquire() as conn:
                async for row in conn.execute(query):
                    print(row)


class ProductService(AbstractService):

    async def get_products(self):
        row = await self.execute(products_table.select().where(
            and_(
                products_table.c.category == 1
            )
        ))

        if row:
            print(row)
            return row
        else:
            return False
