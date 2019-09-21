from django.urls import path, include
from rest_framework import routers

from .views import ApplyViewSet, ApplyTermViewSet

router = routers.DefaultRouter()
router.register('apply', ApplyViewSet)
router.register('term', ApplyTermViewSet)

urlpatterns = [
    path('', include(router.urls))
]
