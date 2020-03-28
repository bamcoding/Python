# visual code에서 지원하는 테스트 러너라는 것을 설정
# 파이썬 기초 핵심 과정 03에서 설명하는 내용
# ctrl+shift+b로 실행이 가능

# 01 print 함수의 사용
# - Separator 옵션
# - end 옵션
# - format
print('T','E','S','T', sep="-", end="")
print('End')

# 괄호의 종류 (소괄호) {중괄호} [대괄호]
print('{} and {}'.format('you','me'))
print("{0} and {1} and {0}".format('you','me'))
print("{a} and {b} and {a}".format(a='you',b='me'))
print("{a:5d} and {b:s} and {a:10d}".format(a=200,b='me'))
# %s %d %f 튜플 사용가능 리스트 안됨
params = ('축서단','장무기',1,10.22)
print("%s는 %s의 %d번째 부인이고 %0.2f미쳤다" % params)
print("%10s"%20000000)

# Escape 문자
# \n, \t, \\, \', \", \b, \000
# 모르는 놈들 \r, \f, \a
print("\"흐\"미\000뭔\\데\n아가야\a 벨 \b소리냐 \b리턴")


print("""이거 왜쓰나요?\
\n몰\t라""")
print('''이거 왜쓰냐고요''')
print("내가 왜 %s" % 'ㅋㅋ')
l0 = [1,2,3,4]
print(l0[-1:2])

print('T','E', sep=comma)


