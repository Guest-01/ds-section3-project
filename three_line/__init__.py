from flask import Flask
from three_line.models import db


def create_app():
    app = Flask(__name__)

    # 설정(DB 등)
    app.secret_key = b"dev"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.app_context().push()
    db.init_app(app)
    db.create_all()

    # 라우팅(뷰):
    from .routes import bp

    app.register_blueprint(bp)

    return app
