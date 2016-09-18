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

    def tearDown(self):
        drop_database()
