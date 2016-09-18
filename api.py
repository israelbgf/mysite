from datetime import datetime

from flask import Flask, request

from core.usecase.create_post_usecase import CreatePostUsecase

app = Flask(__name__)


class CreatePostPresenter(object):
    def create_response(self):
        pass


@app.route('/blog/', methods=['POST'])
def create_post():
    presenter = CreatePostPresenter()
    usecase = CreatePostUsecase(presenter, None, datetime.today())

    usecase.execute(**request.get_json())
    return presenter.create_response()


if __name__ == '__main__':
    app.run()
