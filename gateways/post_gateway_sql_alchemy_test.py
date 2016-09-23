from datetime import datetime
from unittest.case import TestCase

from hamcrest import *
from sqlalchemy import select

from gateways.database.tables import Post
from gateways.post_gateway_sql_alchemy import PostGatewaySQLAlchemy
from utils.database_testing import create_database, drop_database

TODAY = datetime.today()


class PostGatewayTest(TestCase):
    def setUp(self):
        self.post_gateway = PostGatewaySQLAlchemy(create_database().connect(), TODAY)

    def test_create_post(self):
        self.post_gateway.save_post({
            'title': ':title:',
            'slug': ':slug:',
            'content': ':content:',
            'date': TODAY})

        assert_that(select([Post]).execute().fetchone(),
                    equal_to((1, ':title:', ':slug:', ':content:', TODAY, TODAY)))

    def test_list_post(self):
        content = {
            'title': ':title:',
            'slug': ':slug:',
            'content': ':content:',
            'date': TODAY,
            'last_updated': TODAY
        }
        Post.insert().values(content).execute()

        posts = self.post_gateway.list_posts()

        assert_that(posts, has_length(1))
        assert_that(posts[0], has_entries({**content, **{'last_updated': TODAY, 'id': 1}}))

    def tearDown(self):
        drop_database()
