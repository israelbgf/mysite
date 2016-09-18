from core.gateways.post_gateway import PostGateway
from gateways.database.tables import Post


class PostGatewaySQLAlchemy(PostGateway):
    def __init__(self, conn, current_timestamp):
        self.conn = conn
        self.current_timestamp = current_timestamp

    def save_post(self, post):
        Post.insert() \
            .values({**post, **{'last_updated': self.current_timestamp}}) \
            .execute()
