from flask import render_template
from app.posts import bp
from app.extensions import db
from app.models.post import Post

# /posts/


@bp.route("/")
def index():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)

# /posts/<id>


@bp.route("/<id>")
def detail(id):
    post = Post.query.get(id)
    return render_template("posts/detail.html", post=post)
