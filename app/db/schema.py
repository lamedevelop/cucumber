from sqlalchemy import (
    Column, Integer, Float, Date,
    Boolean, MetaData, String, Table,
)

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(column_0_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s'
}

metadata = MetaData(naming_convention=convention)


clients_table = Table(
    'clients',
    metadata,
    Column('client_id', Integer, primary_key=True, nullable=False, autoincrement=True),
    Column('name', String(255), nullable=False, default=''),
    Column('surname', String(255), nullable=False, default=''),
    Column('phone', String(20), nullable=False),
    Column('email', String(255), nullable=False, default=''),

)

products_table = Table(
    'products',
    metadata,
    Column('product_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
    Column('price', Integer, nullable=False),
    Column('category', Integer, nullable=False),
    Column('availability', Boolean, nullable=False),
)

orders_table = Table(
    'orders',
    metadata,
    Column('order_id', Integer, primary_key=True, autoincrement=True),
    Column('client_id', Integer, nullable=False),
    Column('date', Integer, nullable=False),
    Column('payment_method', Integer, nullable=False),
)

order_list_table = Table(
    'order_list',
    metadata,
    Column('order_id', Integer, nullable=False),
    Column('product_id', Integer, nullable=False),
    Column('quantity', Integer, nullable=False),
)

addresses_table = Table(
    'addresses',
    metadata,
    Column('client_id', Integer, nullable=False),
    Column('address', String(255), nullable=False, default=''),
)

categories_table = Table(
    'categories',
    metadata,
    Column('category_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255), nullable=False),
)
