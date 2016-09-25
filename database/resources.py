class SQLAlchemyResource:
    def __init__(self, connection_pool):
        self._connection_pool = connection_pool

    def get_connection(self):
        return self._connection_pool.connect()
