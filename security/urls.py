from django.urls import re_path,include
from rest_framework.routers import DefaultRouter

from security.views import TestingView, ActivityViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'activity', ActivityViewSet),
router.register(r'notification', NotificationViewSet)

urlpatterns = [
    re_path(r'^testing/', TestingView.as_view(), name='testing'),

]
urlpatterns += router.urls