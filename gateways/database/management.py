import flask
from sqlalchemy import create_engine

from gateways.database.tables import metadata


def setup_database():
    engine = create_engine('sqlite:///:memory:')
    metadata.bind = engine
    return engine


def get_conn():
    return flask.current_app.database.connect()


def teardown_database(error):
    flask.current_app.database.dispose()
