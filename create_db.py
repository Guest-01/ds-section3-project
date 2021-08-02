"""
docker-compose에서 command로 실행하기 위한 모듈
"""

from three_line import db, create_app

print('create table if not exists...')
db.create_all(app=create_app())
print('done!')