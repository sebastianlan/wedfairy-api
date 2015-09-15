from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter
from map import views

router = DefaultRouter()
router.register(r'map', views.MapViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)