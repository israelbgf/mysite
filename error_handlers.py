import ujson

import falcon


def invalid_input_for_usecase(exception, request, response, params):
    response.body = ujson.dumps({key: value for (key, value) in exception.errors})
    response.status = falcon.HTTP_UNPROCESSABLE_ENTITY


def unhandled_entity_not_found(exception, request, response, params):
    response.status = falcon.HTTP_NOT_FOUND
