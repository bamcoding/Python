import random
import sqlite3
import datetime
import time
import winsound

words = []
n = 3
midle = n/2
passcnt = 0

with open('./resource/word.txt') as f:
    for c in f:
        words.append(c.strip())

answer = input('Start Game please input username!\n')
print('Hello~',answer)        
username = answer
starttime = datetime.datetime.now()
st = time.time()

for i in range(0,n):
    random.shuffle(words)
    q = random.choice(words)
    print("*Question # {}".format(i+1))
    print(q)
    x = input()
    
    if(q == x.strip()):
        print("Pass!")
        winsound.PlaySound('./sound/good.wav',winsound.SND_FILENAME)
        passcnt +=1
    else:
        winsound.PlaySound('./sound/bad.wav',winsound.SND_FILENAME)
        print("Wrong!")

fm = '%Y-%m-%d %H:%M:%S'
endtime = datetime.datetime.now()
et = time.time() - st
print()
print("게임 시간 :",format(et,".3f"),"맞춘 개수 :",passcnt,"/",n)
starttime = starttime.strftime(fm)
endtime = endtime.strftime(fm)

failcnt = n - passcnt

if passcnt >= midle:
    result = 'Win'
else:
    result = 'Lose' 
print('%s is %s' % (username,result))

score = 100/n
score = passcnt * score
print("%s's score is %.2f" % (username,score))
conn = sqlite3.connect('C:\Dev\database.db')
cursor = conn.cursor()
# cursor.execute('create table GameHistory(id integer primary key autoincrement, username text, score text, passcnt text, failcnt text,result text,starttime text ,endtime text)')
# id, username, score
# , passcnt, failcnt
# , result, starttime, endtime
params = (username,score,passcnt,failcnt,result,starttime,endtime)
cursor.execute('insert into GameHistory( \
    username, score, passcnt, failcnt, result, starttime, endtime) \
    values(?,?,?,?,?,?,?)',params)
conn.commit()
conn.close()