from flask import Flask
from config import Config
from app.extensions import db
import app.models


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.main import bp as main_blueprint
    from app.posts import bp as posts_blueprint
    from app.categories import bp as categories_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(posts_blueprint, url_prefix="/posts")
    app.register_blueprint(categories_blueprint, url_prefix="/categories")

    @app.route("/ping")
    def ping():
        return "It works"

    return app
