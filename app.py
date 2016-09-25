import os

import falcon
from sqlalchemy import create_engine
from werkzeug.serving import run_simple

from api import PostResource
from database.schema import metadata


def create_app():
    engine = create_engine('sqlite:///:memory:')
    metadata.bind = engine
    if os.environ.get('CREATE_DATABASE'):
        metadata.create_all()

    app = falcon.API()
    app.add_route('/blog/post', PostResource(engine))

    return app


if __name__ == '__main__':
    run_simple('localhost', 5000, create_app(), use_reloader=True)
