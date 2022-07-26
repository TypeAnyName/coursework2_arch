from app.container import comments_service
from app.schemas.comments import CommentsSchema
from flask_restx import Resource, Namespace

comments_ns = Namespace('comments')


@comments_ns.route('/')
class CommentsView(Resource):
    def get(self):
        coments = comments_service.get_all()
        return CommentsSchema(many=True).dump(coments), 200


@comments_ns.route('/<int:cid>/')
class PostView(Resource):
    def get(self, cid):
        b = comments_service.get_one(cid)
        sm_d = CommentsSchema().dump(b)
        return sm_d, 200
