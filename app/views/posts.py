from flask import request

from app.container import posts_service
from app.schemas.posts import PostsSchema
from flask_restx import Resource, Namespace

posts_ns = Namespace('posts')


@posts_ns.route('/')
class PostsView(Resource):
    def get(self):
        posts = posts_service.get_all()
        return PostsSchema(many=True).dump(posts), 200


@posts_ns.route('/<int:pid>/')
class PostView(Resource):
    def get(self, pid):
        b = posts_service.get_one(pid)
        sm_d = PostsSchema().dump(b)
        return sm_d, 200
