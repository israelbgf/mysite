from unittest.case import TestCase

import ujson

from api import app


class CreatePostTests(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_should_create_new_post(self):
        response = self.app.post('/blog/', data=ujson.dumps({
            'title': 'Welcome!',
            'content': 'lore ipsum',
            'slug': 'first-post'
        }), headers={'Content-Type': 'application/json'})

        self.assertEqual(200, response.status_code)
