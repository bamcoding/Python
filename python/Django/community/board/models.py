from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=60,verbose_name='제목')
    description = models.CharField(max_length=100,verbose_name='내용',null=True)
    createdts = models.DateTimeField(auto_now_add=True,verbose_name='생성일시',null=True)
    modifiedts = models.DateTimeField(auto_now_add=True,verbose_name='수정일시',null=True)

    def __str__(self):
        return '게시판'

    class Meta:
        db_table = 'django_board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'