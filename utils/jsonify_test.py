from datetime import datetime, date
from unittest.case import TestCase

from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to

from utils.jsonify import jsonify


class JsonifyTests(TestCase):
    def test_convert_datetime(self):
        string = jsonify({"datetime": datetime(2016, 12, 25, 0, 0, 0)})
        assert_that(string, equal_to('{"datetime": "2016-12-25 00:00:00"}'))

    def test_convert_date(self):
        string = jsonify({"date": date(2016, 12, 25)})
        assert_that(string, equal_to('{"date": "2016-12-25 00:00:00"}'))
