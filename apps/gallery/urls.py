from django.urls import path, include
from rest_framework import routers

from .views import GalleryViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('gallery', GalleryViewSet)
router.register('image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
