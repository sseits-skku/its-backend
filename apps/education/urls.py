from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, EducationViewSet, EducationDownloadView

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('', EducationViewSet)

urlpatterns = [
    path('download/<int:id>', EducationDownloadView.as_view()),
    path('', include(router.urls))
]
