from django.conf.urls import url, patterns, include
from aidaijia_coupon import views


urlpatterns = patterns(
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^aidaijia_coupon/$', views.create_coupon),
    url(r'^aidaijia_coupon/(?P<pk>[a-z0-9]+)/$', views.retrieve_coupon),
)