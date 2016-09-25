from unittest.case import TestCase

from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.object.haslength import has_length
from voluptuous.schema_builder import Required

from core.utils.usecase import Usecase, InvalidInputException


class SampleUsecase(Usecase):
    pass


class UsecaseTests(TestCase):
    def test_throws_invalid_input_exception_when_schema_is_invalid(self):
        SampleUsecase.schema = {"foo": int, Required("bar"): str}

        with self.assertRaises(InvalidInputException) as context:
            SampleUsecase().execute({"foo": "???"})

        assert_that(context.exception.errors, has_length(2))
        assert_that(context.exception.errors[0], equal_to(('foo', 'expected int')))
        assert_that(context.exception.errors[1], equal_to(('bar', 'required key not provided')))
