from datetime import datetime

from flask import Flask, request

from core.usecase.create_post_usecase import CreatePostUsecase
from gateways.database.management import get_conn, teardown_database, setup_database
from gateways.database.tables import metadata
from gateways.post_gateway_sql_alchemy import PostGatewaySQLAlchemy
from presenters.empty_presenter_api import EmptyPresenterAPI


def create_app():
    app = Flask(__name__)
    app.database = setup_database()
    metadata.create_all()
    app.teardown_appcontext(teardown_database)
    return app


app = create_app()


@app.route('/blog/', methods=['POST'])
def create_post():
    current_timestamp = datetime.today()
    presenter = EmptyPresenterAPI()
    usecase = CreatePostUsecase(presenter,
                                PostGatewaySQLAlchemy(get_conn(), current_timestamp),
                                current_timestamp)

    usecase.execute(request.get_json())
    return presenter.create_response()


if __name__ == '__main__':
    app.run()
