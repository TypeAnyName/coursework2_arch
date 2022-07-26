from app.dao.models import Comments


class CommentsDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, cid):
        return self.session.query(Comments).get(cid)

    def get_all(self):
        return self.session.query(Comments).all()

    def get_by_pid(self, pid):
        return self.session.query(Comments).filter(Comments.post_id == pid).all()
