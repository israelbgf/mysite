from sqlalchemy import create_engine

from database.schema import metadata

engine = None


def create_database():
    engine = create_engine('sqlite:///:memory:')
    metadata.bind = engine
    metadata.create_all()
    return engine


def drop_database():
    if engine:
        engine.dispose()
