from django.shortcuts import render
from .models import Board
from .serializers import BoardSerializers
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView,UpdateAPIView, DestroyAPIView
# Create your views here.

class BoardRestList(ListAPIView):
  queryset = Board.objects.all()
  serializer_class = BoardSerializers

class BoardRestCreate(CreateAPIView):
  queryset = Board.objects.all()
  serializer_class = BoardSerializers

class BoardRestDetail(RetrieveAPIView):
  queryset = Board.objects.all()
  serializer_class = BoardSerializers

class BoardRestUpdate(UpdateAPIView):
  queryset = Board.objects.all()
  serializer_class = BoardSerializers

class BoardRestDelete(DestroyAPIView):
  queryset = Board.objects.all()
  serializer_class = BoardSerializers
