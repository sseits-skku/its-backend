from django.urls import path, include
from rest_framework import routers

from .views import GalleryViewSet, ImageViewSet, ImageDownloadView

router = routers.DefaultRouter()
router.register('image', ImageViewSet)
router.register('', GalleryViewSet)

urlpatterns = [
    path('image/download/<int:id>', ImageDownloadView.as_view()),
    path('', include(router.urls))
]
