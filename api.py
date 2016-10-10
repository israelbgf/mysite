import ujson
from datetime import datetime

import falcon

from core.usecase.create_post_usecase import CreatePostUsecase
from database.resources import SQLAlchemyResource
from gateway.post_gateway_sql_alchemy import PostGatewaySQLAlchemy
from presenter.empty_presenter_api import BlankResponsePresenterAPI
from util.jsonify import jsonify


class PostResource(SQLAlchemyResource):
    def on_post(self, request, response):
        current_timestamp = datetime.today()
        presenter = BlankResponsePresenterAPI()
        gateway = PostGatewaySQLAlchemy(self.get_connection(), current_timestamp)
        usecase = CreatePostUsecase(presenter, gateway, current_timestamp)

        usecase.execute(ujson.loads(request.stream.read()))

        response.status = falcon.HTTP_CREATED

    def on_get(self, request, response):
        gateway = PostGatewaySQLAlchemy(self.get_connection(), datetime.today())

        response.body = jsonify(gateway.list_posts())
        response.status = falcon.HTTP_OK


class SinglePostResource(SQLAlchemyResource):
    def on_get(self, request, response, identifier):
        gateway = PostGatewaySQLAlchemy(self.get_connection(), datetime.today())

        try:
            post = gateway.find_post_by_id(int(identifier))
        except ValueError:
            post = gateway.find_post_by_slug(identifier)

        response.body = jsonify(post)
        response.status = falcon.HTTP_OK
