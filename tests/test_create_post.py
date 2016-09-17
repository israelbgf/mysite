from tests.base import APITestCase


class CreatePostTests(APITestCase):
    def test_should_create_new_post(self):
        response = self.client.post('/blog/2016/12/', data={
            'title': 'Welcome!',
            'content': 'lore ipsum',
            'slug': 'first-post'
        })
        self.assertEqual(200, response.status_code)
