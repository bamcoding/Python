from django.urls import path
from . import views

urlpatterns = [
    path('write/', views.write),
    path('detail/<int:bpk>', views.detail)
]