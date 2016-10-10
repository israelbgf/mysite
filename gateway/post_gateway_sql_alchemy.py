from sqlalchemy import select

from core.gateways.post_gateway import PostGateway
from database.schema import Post
from core.exceptions import PostNotFoundException


class PostGatewaySQLAlchemy(PostGateway):
    def __init__(self, conn, current_timestamp):
        self.conn = conn
        self.current_timestamp = current_timestamp

    def save_post(self, post):
        Post.insert() \
            .values({**post, **{'last_updated': self.current_timestamp}}) \
            .execute()

    def list_posts(self):
        return [dict(row) for row in select([
            Post.c.id, Post.c.title, Post.c.slug,
            Post.c.date, Post.c.last_updated]).execute().fetchall()]

    def find_post_by_slug(self, slug):
        result = select([Post]).where(Post.c.slug == slug).execute().fetchone()
        if result:
            return dict(result)
        else:
            raise PostNotFoundException

    def find_post_by_id(self, id):
        result = select([Post]).where(Post.c.id == id).execute().fetchone()
        if result:
            return dict(result)
        else:
            raise PostNotFoundException
