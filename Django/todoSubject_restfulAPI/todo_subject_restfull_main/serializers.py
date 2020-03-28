from .models import TodoList
from rest_framework import serializers

class TodoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = TodoList
    fields = ('no','title')