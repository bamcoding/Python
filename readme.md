 # 프레임워크란 무엇인가?
자주 사용되는 코드를 체계화하여 쉽게 사용할 수 있도록 도와주는 코드의 집합
라이브러리와 혼동될 수 있지만 규모가 크고 프로젝트의 기반이 됩니다.
건축에 비유하면 구조를 만드는 골조가 프레임워크라면
그외 자재들이 라브이브러리가 됨

 # 파이썬 핵심
 1. 가상환경을 왜 사용하는가?
	- 가상 개발 환경은 프로젝트 간에 충돌을 방지한다.
 1. 가상환경 종류
	 - venv : Python 3.3 버전 이후 부터 기본모듈
	 - virtualenv : Python 2 버전부터 사용해오던 가상환경 라이브러리
	 - conda : Anaconda Python 기본모듈
	 - pyenv : Python Version Manger, 가상환경 기능을 플러그인 형태로 제공
 1. 가상환경 설정하기
	 - pip -m venv __[가상환경 폴더명]__ 
	 - pip install virtualenv > virtualenv __[가상환경 폴더명]__
 1. 가상환경 실행하기
	- __[가상환경 폴더명]__\Script(맥os는 bin)\activate

 # 장고
 1. 프로젝트 생성 > django_admin startproject [프로젝트명]
 1. 앱 생성 > django_admin startapp [앱명]
 1. templates
	- 메인 프로젝트 urls.py에서 각 앱 urls.py를 호출합니다.
	- 각 앱 urls.py는 각 views.py를 호출하고 views.py는 함수를 실행하여
	- templates 엔진을 통해 templates 폴더에 만들어지는 html파일을 리턴합니다.
	- 메인 프로젝트의 setting.py, urls.py에 앱, 모델 생성시 설정을 추가해야합니다.
	- 장고는 admin 화면을 제공하는 프레임워크입니다.
	- 각 앱에서 admin.py를 생성하여 admin 화면에 전시할 수 있습니다.
	- 화면에 전시하기 전에 DB를 생성해야 합니다. 
	- manage.py makemigrations DB 생성전 설정
	- manage.py migrate DB 생성