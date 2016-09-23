from datetime import datetime

from flask import request

from app import app
from core.usecase.create_post_usecase import CreatePostUsecase
from gateways.database.conn_management import get_conn
from gateways.post_gateway_sql_alchemy import PostGatewaySQLAlchemy
from presenters.empty_presenter_api import BlankResponsePresenterAPI
from utils.jsonify import jsonify


@app.route('/blog/', methods=['POST'])
def create_post():
    current_timestamp = datetime.today()
    presenter = BlankResponsePresenterAPI()
    gateway = PostGatewaySQLAlchemy(get_conn(), current_timestamp)
    usecase = CreatePostUsecase(presenter, gateway, current_timestamp)

    usecase.execute(request.get_json())
    return presenter.create_response()


@app.route('/blog/', methods=['GET'])
def list_posts():
    gateway = PostGatewaySQLAlchemy(get_conn(), datetime.today())
    return jsonify(gateway.list_posts())
