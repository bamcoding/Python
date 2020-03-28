# 03 가상환경 설정 및 패키지 설치
# 가상환경을 왜 쓰는가?
# 어떤 운영체제를 쓰던간에
print("하나의 운영체제에 여러 프로젝트 \
\n모듈을 설치하다보면 프로젝트간의 충돌이 \
\n발생할 수도 있기 때문에 가상환경을 생성하여 \
\n각 프로젝트 간에 충돌을 없앤다 \
\n운영체제와 상관없이 \
\n각 프로젝트에 필요한 모듈만 설치해 사용 가능하다")

print("{}에서는 {}로 경로 이동".format('cmd','cd'))
print("%s 명령어로 %s을 생성"%('python -m venv path', '가상환경'))
print("{a:s}".format(a="activate"))

# 가상환경에 패키지 설치
simplejson = '패키지'
# 이미 개발되어 있는 것을 가져와서
# 빠르게 개발하는 것도 개발 요령
# pip search simplejson
# pip search simple*
# pip install simplejson
# pip install --upgrade simplejson
# pip uninstall simplejson
# pip list
# pip show simplejson
print("%s"%"명령어 5개는 외워야 합니다")
print("1.pip list\n\
2.pip search\n\
3.pip install\n\
4.pip uninstall\n\
5.pip show\n")
