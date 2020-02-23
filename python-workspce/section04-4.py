# 집합(Sets) (순서X 중복X)
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6])

print(type(a))
#중복을 허용하지 않는다
print(c)

t= tuple(b)
print(t)
l= list(c)
print(l)

print('b:', end='')
print(list(b))
print('c:', end='')
print(list(c))

s1 = b.intersection(c)
print(s1)
s2 = b.difference(c)
print(s2)
print('b:', end='')
print(b)
print('c:', end='')
print(c)
s3 = b.union(c)
print(s3)
a=set([1,2,3,4,5])
b=set([3,4,5,6,7])
s3 = a|b
print(s3)

# 추가 & 제거
s1 = set([1,2,3])
print(s1)
s1.add(18)
print(s1)
s1.remove(1)
print(s1)

# 순서 중복 수정 삭제
# 튜플 수정x 삭제x
# 딕셔너리 중복x 순서x
# 셋은 중복X 순서X