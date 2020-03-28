from django.shortcuts import render
from .models import TodoList
from .serializers import TodoSerializer
from rest_framework import viewsets

class Todo_subject_restfull_main(viewsets.ModelViewSet):
  queryset = TodoList.objects.all()
  serializer_class = TodoSerializer