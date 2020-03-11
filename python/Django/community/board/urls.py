from django.urls import path
from . import views

urlpatterns = [
    path('boardwrite/', views.boardwrite),
    path('detail/<int:pk>', views.boarddetail)
]