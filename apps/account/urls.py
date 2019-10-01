from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, user_view

router = routers.DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('which', user_view),
    path('', include(router.urls)),
]
