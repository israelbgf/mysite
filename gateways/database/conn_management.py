import flask


def get_conn():
    request_context = flask.g
    if hasattr(request_context, 'conn'):
        return request_context.conn
    request_context.conn = flask.current_app.connection_pool.connect()
    return request_context.conn


def close_opened_connection(error):
    request_context = flask.g
    if hasattr(request_context, 'conn'):
        request_context.conn.close()
