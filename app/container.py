from app.dao.posts import PostsDao
from app.dao.comments import CommentsDao
from app.services.posts import PostsService
from app.services.comments import CommentsService
from app.setup_db import db


posts_dao = PostsDao(session=db.session)
comments_dao = CommentsDao(session=db.session)

posts_service = PostsService(posts_dao=posts_dao)
comments_service = CommentsService(comments_dao=comments_dao)
