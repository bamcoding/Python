from django.db import models

# Create your models here.
class TodoList(models.Model):
  no = models.AutoField(db_column='NO', primary_key=True)
  title = models.CharField(db_column='TITLE',max_length=200, blank=True, null=True)