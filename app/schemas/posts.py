from marshmallow import Schema, fields


class PostsSchema(Schema):
    id = fields.Int()
    poster_name = fields.Str()
    poster_avatar = fields.Str()
    pic = fields.Str()
    content = fields.Str()
    views_count = fields.Int()
    likes_count = fields.Int()