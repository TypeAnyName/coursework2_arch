from flask import current_app
from sqlalchemy import desc

from app.dao.models import Posts


class PostsDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, pid):
        return self.session.query(Posts).get(pid)

    def get_all(self,):
        return self.session.query(Posts).all()

    def get_by_username(self, username):
        return self.session.query(Posts).filter(Posts.poster_name == username).all()

    def get_by_content(self, query):
        return self.session.query(Posts).filter(Posts.content.like(query)).all()
