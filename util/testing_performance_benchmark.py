from datetime import datetime
from unittest.mock import create_autospec

from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String, Text, DateTime

metadata = MetaData()

tables = []
for i in range(30):
    tables.append(Table('post' + str(i), metadata,
                        Column('id', Integer, primary_key=True),
                        Column('title', String(100)),
                        Column('slug', String(50)),
                        Column('content', Text()),
                        Column('date', DateTime()),
                        Column('last_updated', DateTime())))

Post = tables[0]


def database_creation_every_time(iterations):
    print('database_creation_every_time')
    start = datetime.now()

    for i in range(iterations):
        engine = create_engine('sqlite:///:memory:')
        metadata.bind = engine
        metadata.create_all()
        content = {
            'title': ':title:',
            'slug': ':slug:',
            'content': ':content:',
        }
        Post.insert().values(content).execute()
        assert len(select([Post]).execute().fetchone()) > 0

        engine.dispose()

    end = datetime.now()
    print('{} seconds'.format((end - start)))


def database_creation_once(iterations):
    print('database_creation_once')
    start = datetime.now()

    engine = create_engine('sqlite:///:memory:')
    metadata.bind = engine
    metadata.create_all()
    for i in range(iterations):
        conn = engine.connect()
        transaction = conn.begin()
        content = {
            'title': ':title:',
            'slug': ':slug:',
            'content': ':content:',
        }
        Post.insert().values(content).execute()
        assert len(conn.execute(select([Post])).fetchone()) > 0
        transaction.rollback()
    engine.dispose()

    end = datetime.now()
    print('{} seconds'.format((end - start)))


def mocking_database(iterations):
    class SampleGateway:
        def foo(self, bar=None):
            pass

    print('mocking_database')
    start = datetime.now()

    for i in range(iterations):
        mock = create_autospec(SampleGateway)
        mock.foo.return_value = "bar"
        assert mock.foo() == "bar"

    end = datetime.now()
    print('{} seconds'.format((end - start)))


if __name__ == '__main__':
    database_creation_every_time(1000)
    database_creation_once(1000)
    mocking_database(1000)
