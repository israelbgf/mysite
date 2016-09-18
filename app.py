import os

from flask import Flask
from sqlalchemy import create_engine

from gateways.database.conn_management import close_opened_connection
from gateways.database.tables import metadata

app = Flask(__name__)
app.connection_pool = create_engine('sqlite:///:memory:')
metadata.bind = app.connection_pool

if os.environ.get('DEVELOPMENT_SERVER'):
    metadata.create_all()

try:
    import api
except Exception as e:
    raise e

app.teardown_appcontext(close_opened_connection)

if __name__ == '__main__':
    app.run()
