from datetime import datetime
from unittest.case import TestCase

from hamcrest import *
from sqlalchemy import select, create_engine

from database.schema import Post, metadata
from gateway.post_gateway_sql_alchemy import PostGatewaySQLAlchemy

TODAY = datetime.today()


class DatabaseTestCase(TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        metadata.bind = self.engine
        metadata.create_all()

    def tearDown(self):
        self.engine.dispose()


class SavePostTest(DatabaseTestCase):
    def setUp(self):
        super(SavePostTest, self).setUp()
        self.post_gateway = PostGatewaySQLAlchemy(self.engine.connect(), TODAY)

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
