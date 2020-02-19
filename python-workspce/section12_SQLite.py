# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

#삽입 날짜 생성
now = datetime.datetime.now()
print('now : ',now)
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ',nowDatetime)

# sqlite3
print('sqlite3.version : ',sqlite3.version)
print('sqlite3.sqlite_version : ',sqlite3.sqlite_version)

# DB 생성 & Auto commit(rollback)
conn = sqlite3.connect('C:\Dev\database.db',isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC INTEGER REAL BLOB)
c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text \
,phone text, website text, regdate text)')

c.execute("INSERT INTO users VALUES(1, 'kim', 'gunj.lee@naver.com','010-0000-0000'\
    ,'www.naver.com',?)",(nowDatetime,))

# 자동 커밋
# isolation_level = None
# 커밋
# conn.commit()
# 롤백
# conn.rollback()
# 접속 해제
# conn.close()