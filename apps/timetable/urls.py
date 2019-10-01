from django.urls import path, include
from rest_framework import routers

from .views import OHTableViewSet

router = routers.DefaultRouter()
router.register('', OHTableViewSet)

urlpatterns = [
    path('', include(router.urls))
]
