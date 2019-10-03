from django.urls import path, include
from rest_framework import routers

from .views import OHTableViewSet, OHEntryViewSet

router = routers.DefaultRouter()
router.register('entry', OHEntryViewSet)
router.register('', OHTableViewSet)


urlpatterns = [
    path('', include(router.urls))
]
