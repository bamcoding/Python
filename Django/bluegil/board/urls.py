from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

app_name = 'board'

# router = routers.DefaultRouter()
# router.register(r'todo_board',views.BoardRestMain)
urlpatterns = [
  url('api-auth/',include('rest_framework.urls')),
  url(r'^$',views.BoardRestList.as_view(),name='list'),
  url(r'^create/$',views.BoardRestCreate.as_view(),name='create'),
  url(r'^(?P<pk>\d+)/$',views.BoardRestDetail.as_view(),name='detail'),
  url(r'^update/(?P<pk>\d+)/$',views.BoardRestUpdate.as_view(),name='update'),
  url(r'^delete/(?P<pk>\d+)/$',views.BoardRestDelete.as_view(),name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)