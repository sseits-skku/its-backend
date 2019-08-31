from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, PermissionViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('group', GroupViewSet)
router.register('permission', PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
