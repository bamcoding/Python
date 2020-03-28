# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3
import datetime

now = datetime.datetime.now()

print(now)

sNow = now.strftime('%Y-%m-%d %H:%M:%S')

print(sNow)

conn = sqlite3.connect('C:\Dev\database.db')
c = conn.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text \
# ,phone text, website text, regdate text)')
# c.execute('insert into users(id, username, email, phone, website, regdate) \
#     values("5","go","hanzen@naver.com","010-0000-0000","hoho@mdmd.com", ?)',(sNow,))
# conn.commit()

# c.execute('select * from users')
# print(c.fetchone())
# print(c.fetchmany(size=3))
# print(c.fetchall())
# print(type(c.fetchall()))

# rows = c.fetchall()
# for row in rows:
#     print(row)
#     print(type(row))

# for row in c.execute('select * from users'):
#     print(row)

params = (3,)
c.execute('select * from users where id=?',params)
print(c.fetchall())

param = 4
c.execute('select * from users where id=%s' % param)
print(c.fetchall())

c.execute('select * from users where id=:id', {"id":"1"})
print(c.fetchall())

# 리스트 파라미터는 안됨
c.execute('select * from users where id in (%s,%s)' % ('1','2'))
print(c.fetchall())


with conn:
    with open('C:/Dev/python-workspce/resource/dump.sql','w') as f:
        for l in conn.iterdump():
            f.write('%s\n' % l)
        print('Dump Print Complete')


