# 02 몸풀기 코딩
# 모듈
# import this
import sys
# 파이썬 기본 인코딩 UTF-8
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 변수, 조건문 사용

isTrue = True
if(isTrue):
  print('True')

#반복문 사용
for i in range(1,10):
  for j in range(i,10):
    print(j,end='')
  print()

#함수사용
def hello():
  print('hello')
hello()

#클래스 사용
class User:
  name = 'user.name'
  def printName(self):
    print(self.name)

# 상속
class Customer(User):
  def printSuperName():
    super.printName()

user = Customer()
user.printName()