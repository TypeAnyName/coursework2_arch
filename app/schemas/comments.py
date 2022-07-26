from marshmallow import Schema, fields

from app.schemas.posts import PostsSchema


class CommentsSchema(Schema):
    id = fields.Int()
    commenter_name = fields.Str()
    comment = fields.Str()
    post_id = fields.Nested(PostsSchema)
