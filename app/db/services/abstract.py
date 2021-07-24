from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker

from app.db.settings import DbSettings


class AbstractService:

    def __init__(self) -> None:
        self.engine = create_engine(DbSettings.conn_string())

    async def execute(self, query):
        with self.engine.connect() as conn:
            return conn.execute(query).fetchone()

    async def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    async def prepare_args(self, args):
        if args is None:
            args = dict()
        return args

    async def select_multi(self, table: Table, args):
        args = await self.prepare_args(args)
        session = await self.get_session()

        rows = session.query(table) \
            .filter_by(**args) \
            .all()

        return rows
