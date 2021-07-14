import aiopg


db_config = {
    'user': 'postgres',
    'password': '1234',
    'database': 'common',
    # 'host': 'db_domain',
    'host': '127.0.0.1',
    'port': '5432',
}


class PoolManager:

    @property
    def conn_string(self):
        return f"postgresql://" \
               f"{db_config['user']}:{db_config['password']}@" \
               f"{db_config['host']}:{db_config['port']}/{db_config['database']}"

    @property
    def dsn(self):
        return f"dbname={db_config['database']} " \
               f"user={db_config['user']} " \
               f"password={db_config['password']} " \
               f"host={db_config['host']}"

    async def execute(self, query):
        async with aiopg.create_pool(self.dsn) as pool:
            async with pool.acquire() as conn:
                cur = await conn.cursor()
                await cur.execute(query)
                return await cur.fetchall()
