# Boolean
# Number
# String
# Byte

v_str1 = 'Niceman'
v_bool = True
v_str2 = 'Goodboy'
v_float = 10.3
v_int = 7
v_dict = {
    'name' : 'Kim'
    ,'age' : 25
}

v_list = [1,2,3]
v_tuple = 1,2,3,
v_set={1,2,3}

print(type(v_set))
print(type(v_float))

i1 = 38
i2 = 939
big_int1 = 999999999999
print(type(big_int1))

print(3**2)

f1 = .2

print(1+f1)
print(type(2+f1))
a= 5.
print(type(a))
result2 = a+4
print(type(result2))

# 자료형의 형변환
print(int(result2))
print(int(True))
print(int(False))
print(float('3'))
print(complex(True))

#단항연산자
x=-1
print(x)
x+=1
print(x)

for x in range(20):
    print(x)

import math
print(math.ceil(5.1))
n,m=divmod(100,9)
print(n,m)

print(10//3)
print(10/3)
print(10%3)