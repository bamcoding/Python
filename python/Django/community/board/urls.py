from django.urls import path
from . import views

urlpatterns = [
    path('boardlist/', views.boardlist)
]