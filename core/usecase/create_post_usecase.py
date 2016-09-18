from core.utils.usecase import Usecase


class CreatePostUsecase(Usecase):

    SUCCESS = 0

    schema = {
        'title': str,
        'slug': str,
        'content': str,
    }

    def __init__(self, presenter, post_gateway, today):
        self.presenter = presenter
        self.post_gateway = post_gateway
        self.today = today

    def do(self, input):
        self.post_gateway.save_post({**input, **{'date': self.today}})
        self.presenter.display(self.SUCCESS)
