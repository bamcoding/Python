# Section07-1
# 클래스 선언 및 self의 이해
# 클래스 선언
# 클래스 네임스페이스 self
# 클래스, 인스턴스 변수
# self

# 선언
# class 클래스명:
#   함수
#   함수
#   함수


# 예제1
class UserInfo:
  # 속성, 메소드
  def __init__(self, name):
    self.name = name
      
  def user_info_p(self):
    print('name : ',self.name)   

  def head(self):
    print(self.name,'머리')
  def hand(self):
    print(self.name,'손')
  def foot(self):
    print(self.name,'발')

user = UserInfo('이근재')
user.head()

user2 = UserInfo('김형우')
user2.foot()

class Customer(UserInfo):
  money = 1000
  def showMoney(self):
    print(self.name,self.money)

c = Customer('고객')
c.name='호구'
c.foot()
c.showMoney()

# 클래스, 인스턴스 차이 중요
# 클래스를 인스턴스화 객체화해서 변수에 할당시켜서 
# 메모리에 올려서 사용한다

# 네임스페이스 클래스를 인스턴스화 할 때 저장되는 독립적인 공간
# 클래스 변수 : 직접 사용가능 객체보다 먼저 생성된다

# 인스턴스 변수 : 객체마다 별도로 존재 인스턴스 생성 후 사용한다
# 인스턴스 메소드 호출
# ex) user = User()
#     user.showName()

# self의 이해
class SelfTest:
  # 클래스 메소드
  def function():
    print('function1')
  # 인스턴스 메소드
  def function2(self):
    print('function2')

s = SelfTest()

SelfTest.function()
s.function2()