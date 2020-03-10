from django.db import models

# Create your models here.

class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=120,verbose_name='제목')
    description = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE
                              ,verbose_name='작성자')
    modifiedts = models.DateTimeField(auto_now_add=True,verbose_name='수정일시')
    createdts = models.DateTimeField(auto_now_add=True,verbose_name='생성일시')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fc_boards'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'