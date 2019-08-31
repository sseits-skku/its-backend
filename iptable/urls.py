from django.urls import path, include
from rest_framework import routers

from .views import IPAddressViewSet

router = routers.DefaultRouter()
router.register('ip-addr', IPAddressViewSet)

urlpatterns = [
    path('', include(router.urls))
]
