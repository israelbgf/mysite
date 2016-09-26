from datetime import datetime
from unittest.case import TestCase

from hamcrest import *
from sqlalchemy import select, create_engine

from core.exceptions import PostNotFoundException
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


class ListPostTest(DatabaseTestCase):
    def setUp(self):
        super(ListPostTest, self).setUp()
        self.post_gateway = PostGatewaySQLAlchemy(self.engine.connect(), TODAY)

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


class FindPostBySlugTest(DatabaseTestCase):
    def setUp(self):
        super(FindPostBySlugTest, self).setUp()
        self.post_gateway = PostGatewaySQLAlchemy(self.engine.connect(), TODAY)

    def test_raise_exception_when_doesnt_find_a_post(self):
        with self.assertRaises(PostNotFoundException):
            self.post_gateway.find_post_by_slug('nice-looking-post')

    def test_find_post(self):
        content = {
            'title': ':title:',
            'slug': 'nice-looking-post',
            'content': ':content:',
            'date': TODAY,
            'last_updated': TODAY
        }
        Post.insert().values(content).execute()

        post = self.post_gateway.find_post_by_slug('nice-looking-post')

        assert_that(post, has_entries({**content, **{'last_updated': TODAY, 'id': 1}}))
