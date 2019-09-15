from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, EducationViewSet


router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('entry', EducationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
