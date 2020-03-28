from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

app_name = 'todo_subject_restfull_main'

router = routers.DefaultRouter()
router.register(r'todo_board',views.Todo_subject_restfull_main)
urlpatterns = [
  url('api-auth/',include('rest_framework.urls')),
  url(r'^$',include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)