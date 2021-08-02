from flask import Flask
from three_line.models import db
from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)
    load_dotenv()

    # 설정(DB 등)
    db_pw = os.getenv('POSTGRES_PASSWORD')
    app.secret_key = os.getenv('FLASK_SECRET')
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{db_pw}@db:5432/postgres"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # 라우팅(뷰):
    from .routes import bp

    app.register_blueprint(bp)

    return app
