from django.urls import path, include
from rest_framework import routers

from .views import ApplyTermViewSet, ApplyViewSet

router = routers.DefaultRouter()
router.register('term', ApplyTermViewSet)
router.register('apply', ApplyViewSet)

urlpatterns = [
    path('', include(router.urls))
]
