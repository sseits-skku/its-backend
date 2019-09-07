from django.urls import path, include
from rest_framework import routers

from .views import AgendaViewSet, LabelViewSet, ActionViewSet


router = routers.DefaultRouter()
router.register('ag', AgendaViewSet)
router.register('label', LabelViewSet)
router.register('action', ActionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
