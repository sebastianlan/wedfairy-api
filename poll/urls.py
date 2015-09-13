from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter
from poll import views

router = DefaultRouter()
router.register(r'poll', views.PollViewSet)
router.register(r'option', views.OptionViewSet)
router.register(r'vote', views.VoteViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)