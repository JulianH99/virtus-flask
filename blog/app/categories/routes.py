from flask import render_template
from app.categories import bp
from app.extensions import db
from app.models.category import Category


@bp.route("/")
def index():
    categories = Category.query.all()
    return render_template("categories/index.html", categories=categories)


@bp.route("/<id>")
def detail(id):
    category = Category.query.get(id)
    posts = category.posts
    return render_template("categories/detail.html", category=category,
                           posts=posts)
