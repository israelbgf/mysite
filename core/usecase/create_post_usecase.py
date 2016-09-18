from core.utils.presenter import Presenter
from core.utils.usecase import Usecase


class CreatePostUsecase(Usecase):
    schema = {
        'title': str,
        'slug': str,
        'content': str,
    }

    def __init__(self, presenter, post_gateway, current_timestamp):
        self.presenter = presenter
        self.post_gateway = post_gateway
        self.current_timestamp = current_timestamp

    def do(self, input):
        self.post_gateway.save_post({**input, **{'date': self.current_timestamp}})
        self.presenter.display(Presenter.SUCCESS)
