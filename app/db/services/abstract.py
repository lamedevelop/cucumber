from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.settings import DbSettings


class AbstractService:

    def __init__(self) -> None:
        self.engine = create_engine(DbSettings.conn_string())

    async def execute(self, query):
        with self.engine.connect() as conn:
            conn.execute(query)

    async def select(self, query):
        with self.engine.connect() as conn:
            return conn.execute(query).fetchone()

    async def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    async def prepare_args(self, args):
        if args is None:
            args = dict()
        return args
