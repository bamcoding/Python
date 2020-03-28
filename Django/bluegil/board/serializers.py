from .models import Board
from rest_framework import serializers

class BoardSerializers(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Board
    fields = ('title','content','createdts','modifiedts')