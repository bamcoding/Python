# sqlite 데이터 베이스 사용
# 해당 프로젝트 경로에 dbfile을 배치하기 위해서
# os로 절대경로를 파악한다.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 절대결로
basedir = os.path.abspath(os.path.dirname(__file__))
# 파일 생성
dbfile = os.path.join(basedir,'db.sqlite')

app = Flask(__name__)

# sqlalchemy 설정값
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+dbfile
# 사용자 요청의 끝에 커밋
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Test(db.Model):
  __tablename__ = 'test_table'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(32), unique=True)

# 데이터베이스 파일 생성
db.create_all()
# python app2.py

@app.route('/')
def hello():
  return 'hello'