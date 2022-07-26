from app.setup_db import db


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    poster_name = db.Column(db.String)
    poster_avatar = db.Column(db.String)
    pic = db.Column(db.String)
    content = db.Column(db.String)
    views_count = db.Column(db.Integer)
    likes_count = db.Column(db.Integer)

    def __repr__(self):
        return f"<Post '{self.poster_name.title()}'>"
