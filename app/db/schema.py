from sqlalchemy import (
    Column, Integer, Float, Date,
    Boolean, MetaData, String, Table,
)
from sqlalchemy.orm import relationship

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
    Column('name', String(255), nullable=False),
    Column('surname', String(255), nullable=False),
    Column('phone', String(255), nullable=False),
    Column('email', String(255), nullable=False),

)

products_table = Table(
    'products',
    metadata,
    Column('product_id', Integer, primary_key=True, autoincrement=True),
    Column('name', Float, nullable=False),
    Column('price', String(255), nullable=False),
    Column('category', String(255), nullable=False),
    Column('availability', Boolean, nullable=False),
)

orders_table = Table(
    'orders',
    metadata,
    Column('order_id', Integer, primary_key=True, autoincrement=True),
    Column('client_id', Integer, nullable=False),
    Column('date', Date, nullable=False),
    Column('payment_method', String(255), nullable=False),
)

order_list_table = Table(
    'order_list',
    metadata,
    Column('order_id', Integer),
    Column('product_id', Integer),
    Column('quantity', Integer)
)

orders_assign_table = Table(
    'adresses',
    metadata,
    Column('client_id', Integer),
    Column('street', String(255), nullable=False),
    Column('city', String(255), nullable=False),
    Column('building', String(255), nullable=False, default=0),
    Column('flat', String(255), nullable=False, default=0),
)
