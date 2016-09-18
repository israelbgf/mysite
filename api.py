from datetime import datetime

from flask import request

from app import app
from core.usecase.create_post_usecase import CreatePostUsecase
from gateways.database.conn_management import get_conn
from gateways.post_gateway_sql_alchemy import PostGatewaySQLAlchemy
from presenters.empty_presenter_api import EmptyPresenterAPI


@app.route('/blog/', methods=['POST'])
def create_post():
    current_timestamp = datetime.today()
    presenter = EmptyPresenterAPI()
    usecase = CreatePostUsecase(presenter,
                                PostGatewaySQLAlchemy(get_conn(), current_timestamp),
                                current_timestamp)

    usecase.execute(request.get_json())
    return presenter.create_response()
