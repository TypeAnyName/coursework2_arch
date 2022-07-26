from app.setup_db import db


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    commenter_name = db.Column(db.String)
    comment = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)

    post = db.relationship("Posts")
