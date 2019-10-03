from django.urls import path, include
from rest_framework import routers

from .views import OHTableViewSet, OHEntryViewSet

router = routers.DefaultRouter()
router.register('', OHTableViewSet)
router.register('entry', OHEntryViewSet)


urlpatterns = [
    path('', include(router.urls))
]
