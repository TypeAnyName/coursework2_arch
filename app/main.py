from flask import Flask, render_template, request
from flask_restx import Api

from app.container import posts_service, comments_service
from app.views.posts import posts_ns
from app.views.comments import comments_ns
from app.config import BaseConfig
from app.setup_db import db

api = Api(title="Flask Course Project 2", doc="/docs")


def create_app(config_object):
    application = Flask(__name__,
                        template_folder="C:/Users/alexg/PycharmProjects/coursework2/templates",
                        static_folder="C:/Users/alexg/PycharmProjects/coursework2/static"
                        )
    application.config.from_object(config_object)

    @application.route('/')
    def index():
        posts_list = posts_service.get_all()
        return render_template("index.html", posts_list=posts_list)

    @application.route('/<int:post_id>')
    def post_page(post_id):
        post = posts_service.get_one(post_id)
        comments = comments_service.get_by_post_id(post_id)
        return render_template("post.html", post=post, comments=comments)

    @application.route("/users/<username>")
    def users_posts(username):
        posts = posts_service.posts_by_user(username)
        return render_template("user-feed.html", posts=posts)

    @application.route('/search')
    def search():
        search_by = request.args['content']
        posts = posts_service.search_by_content(search_by)
        return render_template("search.html", search_by=search_by, posts=posts)

    register_extensions(application)

    return application


def register_extensions(application):
    db.init_app(application)
    api.init_app(application)
    api.add_namespace(posts_ns)
    api.add_namespace(comments_ns)


if __name__ == '__main__':
    app_config = BaseConfig()
    app = create_app(app_config)
    app.run()