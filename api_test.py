import ujson
from unittest.case import TestCase

from app import app
from utils.database_testing import create_database, drop_database


class CreatePostTests(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        create_database()

    def test_should_create_new_post(self):
        response = self.app.post('/blog/', data=ujson.dumps({
            'title': 'Welcome!',
            'content': 'lore ipsum',
            'slug': 'first-post'
        }), headers={'Content-Type': 'application/json'})

        self.assertEqual(200, response.status_code)

    def tearDown(self):
        drop_database()
