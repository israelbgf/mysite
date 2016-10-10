from datetime import datetime, timedelta
from unittest.case import TestCase

from hamcrest import *
from sqlalchemy import select, create_engine

from core.exceptions import PostNotFoundException
from database.schema import Post, metadata
from gateway.post_gateway_sql_alchemy import PostGatewaySQLAlchemy

NOW = datetime.today()
YESTERDAY = NOW + timedelta(days=-1)


class DatabaseTestCase(TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        metadata.bind = self.engine
        metadata.create_all()

    def tearDown(self):
        self.engine.dispose()


class PostGatewayTestCase(DatabaseTestCase):
    def setUp(self):
        super(PostGatewayTestCase, self).setUp()
        self.post_gateway = PostGatewaySQLAlchemy(self.engine.connect(), NOW)


class SavePostTest(PostGatewayTestCase):
    def test_create_post(self):
        self.post_gateway.save_post({
            'title': ':title:',
            'slug': ':slug:',
            'content': ':content:',
            'date': NOW})

        assert_that(select([Post]).execute().fetchone(),
                    equal_to((1, ':title:', ':slug:', ':content:', NOW, NOW)))


class ListPostTest(PostGatewayTestCase):
    def test_list_post(self):
        content = {
            'title': ':title:',
            'slug': ':slug:',
            'content': ':content:',
            'date': YESTERDAY,
            'last_updated': NOW
        }
        Post.insert().values(content).execute()

        posts = self.post_gateway.list_posts()

        assert_that(posts, has_length(1))
        assert_that(posts[0], has_entries({
            'id': 1,
            'title': ':title:',
            'slug': ':slug:',
            'date': YESTERDAY,
            'last_updated': NOW
        }))


class FindPostBySlugTest(PostGatewayTestCase):
    def test_raise_exception_when_doesnt_find_a_post(self):
        with self.assertRaises(PostNotFoundException):
            self.post_gateway.find_post_by_slug('nice-looking-post')

    def test_find_post(self):
        content = {
            'title': ':title:',
            'slug': 'nice-looking-post',
            'content': ':content:',
            'date': YESTERDAY,
            'last_updated': NOW
        }
        Post.insert().values(content).execute()

        post = self.post_gateway.find_post_by_slug('nice-looking-post')

        assert_that(post, has_entries({**content, **{'last_updated': NOW, 'id': 1}}))


class FindPostByIdTest(PostGatewayTestCase):
    def test_raise_exception_when_doesnt_find_a_post(self):
        with self.assertRaises(PostNotFoundException):
            self.post_gateway.find_post_by_id(999)

    def test_find_post(self):
        content = {
            'title': ':title:',
            'slug': 'nice-looking-post',
            'content': ':content:',
            'date': YESTERDAY,
            'last_updated': NOW
        }
        id = Post.insert().values(content).execute().inserted_primary_key[0]

        post = self.post_gateway.find_post_by_id(id)

        assert_that(post, has_entries({**content, **{'last_updated': NOW, 'id': 1}}))
