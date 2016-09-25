import falcon
from sqlalchemy import create_engine
from werkzeug.serving import run_simple

from api import PostResource
from database.schema import metadata


def create_app(connection_url):
    engine = create_engine(connection_url, echo=True)
    metadata.bind = engine

    app = falcon.API()
    app.add_route('/blog/post', PostResource(engine))
    return app


if __name__ == '__main__':
    app = create_app(connection_url='sqlite:///test.db')
    metadata.create_all()
    run_simple('localhost', 5000, app, use_reloader=True)
