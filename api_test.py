import ujson
from datetime import date
from unittest.case import TestCase

from hamcrest import has_length
from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection.isdict_containingentries import has_entries

from app import app
from gateways.post_gateway_sql_alchemy import PostGatewaySQLAlchemy
from utils.database_testing import create_database, drop_database


class IntegratedTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.conn_pool = create_database()
        self.conn = self.conn_pool.connect()

    def tearDown(self):
        drop_database()


class CreatePostTests(IntegratedTest):
    def test_should_create_new_post(self):
        response = self.app.post('/blog/', data=ujson.dumps({
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

        response = self.app.get('/blog/')

        assert_that(response.status_code, equal_to(200))
        content = ujson.loads(response.data)
        assert_that(content, has_length(1))
        assert_that(content[0], has_entries({
            'title': 'Welcome!',
            'content': 'lore ipsum',
            'slug': 'first-post',
            'date': '2016-12-25 00:00:00'
        }))
