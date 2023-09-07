from django.urls import re_path
from rest_framework.routers import DefaultRouter

from security.views import TestingView

router = DefaultRouter()

urlpatterns = [
    re_path(r'^testing/', TestingView.as_view(), name='testing'),

]
urlpatterns += router.urls