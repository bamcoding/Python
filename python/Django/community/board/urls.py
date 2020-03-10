from django.urls import path
from . import views

urlpatterns = [
    path('boardwrite/', views.boardwrite)
]