
db_config = {
    'user': 'postgres',
    'password': '1234',
    'database': 'common',
    # 'host': 'db_domain',
    'host': '127.0.0.1',
    'port': '5432',
}


class DbSettings:

    @staticmethod
    def conn_string() -> str:
        return f"postgresql://" \
               f"{db_config['user']}:{db_config['password']}@" \
               f"{db_config['host']}:{db_config['port']}/{db_config['database']}"

    @staticmethod
    def dsn() -> str:
        return f"dbname={db_config['database']} " \
               f"user={db_config['user']} " \
               f"password={db_config['password']} " \
               f"host={db_config['host']}"

    @staticmethod
    def params():
        return db_config
