from django.db import models

# Create your models here.
class Board(models.Model):
  objects = models.Manager()
  title = models.CharField(verbose_name='제목',max_length=100)
  content = models.CharField(verbose_name='내용',max_length=300)
  createdts = models.DateField(auto_now_add=True,verbose_name='생성일시')
  modifiedts = models.DateField(auto_now_add=True,verbose_name='수정일시')

  class Meta:
    db_table = 'boards'