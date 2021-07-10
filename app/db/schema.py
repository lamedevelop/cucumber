from sqlalchemy import (
    Column, Integer, Float,
    Boolean, MetaData, Table,
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


orders_table = Table(
    'orders',
    metadata,
    Column('order_id', Integer, primary_key=True),
    Column('weight', Float, nullable=False),
    Column('region_id', Integer, nullable=False),
    Column('is_ready', Boolean, nullable=False, default=0),
    Column('complete_time', Integer, nullable=True, default=0),
    Column('assign_id', Integer, nullable=True, default=-1),
)
