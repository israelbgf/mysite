from datetime import datetime
from unittest.case import TestCase

from hamcrest import *
from sqlalchemy import select, create_engine

from gateways.database.tables import Post, metadata
from gateways.post_gateway_sql_alchemy import PostGatewaySQLAlchemy

TODAY = datetime.today()


class PostGatewayTest(TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        metadata.bind = self.engine
        metadata.create_all()
        self.post_gateway = PostGatewaySQLAlchemy(self.engine.connect(), TODAY)

    def test_create_post(self):
        self.post_gateway.save_post({
            'title': ':title:',
            'slug': ':slug:',
            'content': ':content:',
            'date': TODAY})

        assert_that(select([Post]).execute().fetchone(),
                    equal_to((1, ':title:', ':slug:', ':content:', TODAY, TODAY)))

    def tearDown(self):
        self.engine.dispose()
