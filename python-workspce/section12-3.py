import sqlite3

conn = sqlite3.connect('C:\Dev\database.db')
cursor = conn.cursor()


def delete(id):
    cursor.execute('delete from users where id=?',(id,))
    conn.commit()
    print('delete!!!')

def select():
    print(cursor.execute('select * from users')
    for r in cursor.fetchall():
        print(r)

select()

cursor.execute('update users \
     set username =:username \
     where id=:id',{'username':'kim','id':'2'})


cnt = cursor.execute('select * from users').rowcount
print(cnt)
for r in cursor.fetchone():
    print(r)

conn.commit()

conn.close()