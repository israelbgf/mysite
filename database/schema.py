from sqlalchemy import *

metadata = MetaData()

Post = Table('post', metadata,
             Column('id', Integer, primary_key=True),
             Column('title', String(100)),
             Column('slug', String(50)),
             Column('content', Text()),
             Column('date', DateTime()),
             Column('last_updated', DateTime()))
