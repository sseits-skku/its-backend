from django.urls import path, include
from rest_framework import routers

from .views import ImageContentViewSet, FileContentViewSet

router = routers.DefaultRouter()
router.register('file', FileContentViewSet)
router.register('image', ImageContentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
