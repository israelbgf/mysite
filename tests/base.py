import unittest

import api


class APITestCase(unittest.TestCase):
    def setUp(self):
        api.app.config['TESTING'] = True
        self.client = api.app.test_client()
