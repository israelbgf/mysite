import ujson
from datetime import date
from unittest import TestCase

from hamcrest import has_length
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.isdict_containingentries import has_entries
from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse

from app import create_app
from database.schema import metadata
from gateway.post_gateway_sql_alchemy import PostGatewaySQLAlchemy


class IntegratedTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Client(create_app(), BaseResponse)

    def setUp(self):
        self.conn = metadata.bind.connect()


class CreatePostTests(IntegratedTest):
    def test_should_create_new_post(self):
        response = self.client.post('/blog/post', data=ujson.dumps({
            'title': 'Welcome!',
            'content': 'lore ipsum',
            'slug': 'first-post'
        }), headers={'Content-Type': 'application/json'})

        assert_that(response.status_code, equal_to(200))


class ListPostsTests(IntegratedTest):
    def test_should_list_existing_posts(self):
        PostGatewaySQLAlchemy(self.conn, date(2016, 12, 25)).save_post({
            'title': 'Welcome!',
            'content': 'lore ipsum',
            'slug': 'first-post',
            'date': date(2016, 12, 25)
        })

        response = self.client.get('/blog/post')

        assert_that(response.status_code, equal_to(200))
        content = ujson.loads(response.data)
        assert_that(content, has_length(1))
        assert_that(content[0], has_entries({
            'title': 'Welcome!',
            'content': 'lore ipsum',
            'slug': 'first-post',
            'date': '2016-12-25 00:00:00'
        }))
