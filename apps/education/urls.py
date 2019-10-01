from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, EducationViewSet, DownloadView

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('', EducationViewSet)

urlpatterns = [
    path('download/<int:id>', DownloadView.as_view()),
    path('', include(router.urls))
]
