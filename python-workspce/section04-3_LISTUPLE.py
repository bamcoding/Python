# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플
# 리스트 (순서, 중복, 수정, 삭제가능)
# 선언

a = []
b = list()
c = [1,2,3,4]
# 데이터 타입이 달라도 저장이 가능
d = [10,100,'Pen','Banana','Orange']
e = [10,100,['Pen','Banana','Orange']]
print(type(a))

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c+d)
print(c*3)
print(str(c[0])+'hello')

# 리스트
name1 = 'Lee'
name2 = 'Park'

# 리스트 수정, 삭제
print(c)
del c[1]
print(c)
c[1:2] = [10,10,10]
c[1:2] = [[10,10,10]]
print(c)

# 리스트 함수
y = [5,2,4,1,3]
print(y)
y.append(6)
print(y)
y.sort()
print(y)
y.remove(1)
print(y)
del y[1]
print(y)
y.pop()
print(y)
y.extend([1,2,3])
print(y)
y.append([1,2,3])
print(y)
y.insert(0,123)
print(y)

# 튜플 
# 리스트랑 똑같은데 몇가지 특징이 있다 
# 순서, 중복 있음 수정, 삭제 없음
a = ()
b = (1,)
c = (1,2,3,4,)
d = (10,100,100,('a','b','c'))

print(type(a))
print(b[0])
print(c[3])
print(c[2])
print(d[1:3])

print(10 in d)
print(d.index(10))
print(d.count(100))
