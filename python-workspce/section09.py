# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 
# 쓰기 모드(기존 파일 삭제) : w, 
# 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로
# 기타 : http://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
content = f.readline()
print(content)
# print(dir(f))
# 반드시 close 리소스 반환
f.close()

print('------------------------------------------')

# 예제2
# with문은 close를 생략해도 된다
with open('./resource/review.txt', 'r') as f:
    c=f.read()
    print(list(c))
    print(iter(c))

print('------------------------------------------')

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

# 예제4
with open('./resource/review.txt', 'r') as f:
    content=f.read()
    print(">",content)
    content=f.read() # 내용 없음
    print(">",content)
    
# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    print(line)
    while line:#값이 없으면 false
        print(line, end='###')
        line = f.readline()

# 예제7
score = []
with open('./resource/score.txt','r') as f:
    for line in f:
        score.append(int(line))   
    print(score) 

print(sum(score)/len(score))
print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일 쓰기
# 예제1
with open('./resource/write.txt','w') as f:
    f.write('write test')

# 예제2
with open('./resource/write.txt','a') as f:
    f.write('write test')

# 예제3
from random import randint
with open('./resource/leegunj.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(0,50))+'\n')

# 예제4
with open('./resource/print.txt','w') as f:    
    print("log test", file=f)

# 예제5
with open('./resource/list.txt','w') as f:
    li = ['hi','hello','baby']
    f.writelines(li)
