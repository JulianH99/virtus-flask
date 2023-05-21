from sqlalchemy.orm import backref
from app.extensions import db


class PostCategory(db.Model):
    __tablename__ = "post_categories"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))

    post = db.relationship("Post", backref=backref("post"))
    category = db.relationship("Category", backref=backref("category"))
