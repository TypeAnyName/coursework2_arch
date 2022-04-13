from flask import Flask, render_template, request
import utils

app = Flask(__name__)


@app.route('/')
def main_page():
    posts_list = utils.get_posts_all()
    return render_template("index.html", posts_list=posts_list)


@app.route('/posts/<int:post_id>')
def post_page(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)
    return render_template("post.html", post=post, comments=comments)


@app.route('/search')
def search():
    search_by = request.args['s']
    posts = utils.search_for_posts(search_by)
    return render_template("search.html", search_by=search_by, posts=posts)




app.run(debug=True)
