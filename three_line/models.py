from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class Summary(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    create_date = db.Column(db.DateTime(), default=func.now())
    modified = db.Column(db.String(128), default="자동 요약됨")
    title = db.Column(db.String(512), default="제목 없음")
    content = db.Column(db.Text())
    result_1 = db.Column(db.String(512))
    result_2 = db.Column(db.String(512))
    result_3 = db.Column(db.String(512))
