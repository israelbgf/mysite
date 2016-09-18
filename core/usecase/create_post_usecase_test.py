from datetime import datetime
from unittest.case import TestCase
from unittest.mock import create_autospec

from core.gateways.post_gateway import PostGateway
from core.usecase.create_post_usecase import CreatePostUsecase
from core.utils.presenter import Presenter

TODAY = datetime.today()


class CreatePostUsecaseTests(TestCase):
    def setUp(self):
        self.presenter = create_autospec(Presenter)
        self.post_gateway = create_autospec(PostGateway)
        self.usecase = CreatePostUsecase(self.presenter, self.post_gateway, TODAY)

    def test_should_create_post_with_date_for_today(self):
        post = {'title': 'nice title',
                'content': 'nice content',
                'slug': 'nice-title'}

        self.usecase.execute(post)

        self.post_gateway.save_post.assert_called_with({**post, **{'date': TODAY}})
        self.presenter.display.assert_called_with(self.usecase.SUCCESS)
