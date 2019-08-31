from django.urls import path, include
from rest_framework import routers

from .views import StockStatusViewSet, \
                   StockTypeViewSet,   \
                   StockViewSet,       \
                   OSTypeViewSet,      \
                   ComputerViewSet

router = routers.DefaultRouter()
router.register('stock-status', StockStatusViewSet)
router.register('stock-type', StockTypeViewSet)
router.register('stock', StockViewSet)
router.register('os-type', OSTypeViewSet)
router.register('computer', ComputerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
