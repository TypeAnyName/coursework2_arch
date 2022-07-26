from app.dao.comments import CommentsDao


class CommentsService:
    def __init__(self, comments_dao: CommentsDao):
        self.comments_dao = comments_dao

    def get_all(self):
        return self.comments_dao.get_all()

    def get_one(self, cid):
        return self.comments_dao.get_one(cid)

    def get_by_post_id(self, pid):
        return self.comments_dao.get_by_pid(pid)

    # def get_by_post_id(self, pid):
    #     comments = self.comments_dao.get_all()
    #     comments_json_list = []
    #     for comment in comments:
    #         if comment["post_id"] == pid:
    #             comments_json_list.append(comment)
    #     return comments_json_list
