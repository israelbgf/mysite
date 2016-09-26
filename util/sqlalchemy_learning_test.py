from asyncio.test_utils import TestCase
from unittest.mock import Mock

from hamcrest.core import assert_that
from hamcrest.library.object.haslength import has_length
from sqlalchemy import create_engine

from database.schema import metadata

LIST_TABLES = "SELECT name FROM sqlite_master WHERE type='table'"


class SQLAlchemyLearningTests(TestCase):
    def test_should_allow_to_dispose_and_reconnect_an_sqlite_database(self):
        engine = Mock()
        try:
            engine = create_engine('sqlite:///:memory:')
            assert_that(list_all_tables(engine), has_length(0))
            engine.dispose()
            engine = create_engine('sqlite:///:memory:')
            assert_that(list_all_tables(engine), has_length(0))
        finally:
            engine.dispose()

    def test_should_allow_two_different_sqlite_db_instances(self):
        engine1, engine2 = Mock(), Mock()
        try:
            engine1 = create_engine('sqlite:///:memory:')
            metadata.create_all(bind=engine1)
            assert_that(list_all_tables(engine1), has_length(1))

            engine2 = create_engine('sqlite:///:memory:')
            assert_that(list_all_tables(engine2), has_length(0))
        finally:
            engine1.dispose()
            engine2.dispose()


def list_all_tables(engine):
    return engine.connect().execute(LIST_TABLES).fetchall()
