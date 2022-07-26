from app.dao.posts import PostsDao


class PostsService:
    def __init__(self, posts_dao: PostsDao):
        self.posts_dao = posts_dao

    def get_all(self):
        return self.posts_dao.get_all()

    def get_one(self, pid):
        return self.posts_dao.get_one(pid)

    def posts_by_user(self, username):
        return self.posts_dao.get_by_username(username)

    def search_by_content(self, query):
        return self.posts_dao.get_by_content(query)

