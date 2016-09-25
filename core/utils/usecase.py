from voluptuous.error import MultipleInvalid
from voluptuous.schema_builder import Schema


class Usecase(object):
    schema = Schema({})

    def execute(self, input=None):
        try:
            self.do(Schema(self.schema)(input or {}))
        except MultipleInvalid as e:
            raise InvalidInputException([(str(error.path[0]), error.error_message)
                                         for error in e.errors])

    def do(self, input):
        raise NotImplementedError


class InvalidInputException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def __repr__(self):
        return str(self.errors)
