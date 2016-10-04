import ujson

import falcon


def invalid_input_exception_handler(exception, request, response, params):
    response.body = ujson.dumps({key: value for (key, value) in exception.errors})
    response.status = falcon.HTTP_UNPROCESSABLE_ENTITY


def entity_not_found_exception_handler(exception, request, response, params):
    response.status = falcon.HTTP_NOT_FOUND
