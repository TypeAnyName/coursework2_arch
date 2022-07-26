from sqlalchemy.exc import IntegrityError

from app.config import DevelopmentConfig
from app.dao.models import Posts, Comments

from app.main import create_app
from app.setup_db import db
from app.utils import read_json

app = create_app(DevelopmentConfig)

data = read_json("fixtures.json")

with app.app_context():
    for comments in data["comments"]:
        db.session.add(Comments(id=comments["pk"],
                                commenter_name=comments["commenter_name"],
                                comment=comments["comment"],
                                post_id=comments['post_id']))
    for posts in data["posts"]:
        db.session.add(Posts(id=posts["pk"],
                             poster_name=posts['poster_name'],
                             poster_avatar=posts["poster_avatar"],
                             pic=posts['pic'],
                             content=posts['content'],
                             views_count=posts["views_count"],
                             likes_count=posts['likes_count']))

    try:
        db.session.commit()
    except IntegrityError:
        print("Fixtures already loaded")
