from django.urls import path, include
from rest_framework import routers

from .views import PlaceViewSet, StatusViewSet, OSTypeViewSet, StockViewSet, ComputerStockViewSet

router = routers.DefaultRouter()
router.register('place', PlaceViewSet)
router.register('status', StatusViewSet)
router.register('ostype', OSTypeViewSet)
router.register('stock', StockViewSet)
router.register('computer', ComputerStockViewSet)

urlpatterns = [
    path('', include(router.urls))
]
