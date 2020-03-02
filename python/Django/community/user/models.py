from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30,verbose_name='이름')
    password = models.CharField(max_length=30,verbose_name='비밀번호')
    createdts = models.DateField(auto_now_add=True, verbose_name='생성일시')

    # 오프젝트를 문자열로 호출시 리턴값
    def __str__(self):
        return '사용자'

    class Meta:
        # 테이블 이름
        db_table = 'django_user' 
        # admin 화면에서 전시되는 user 테이블명
        verbose_name = '장고 사용자' 
        # admin 화면에서 전시되는 users 테이블명
        verbose_name_plural = '장고 사용자'
        