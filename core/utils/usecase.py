from voluptuous.schema_builder import Schema


class Usecase(object):
    schema = Schema({})

    def execute(self, input=None):
        self.do(Schema(self.schema)(input or {}))

    def do(self, input):
        raise NotImplementedError
