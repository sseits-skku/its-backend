from django.urls import path, include
from rest_framework import routers

from .views import UploadViewSet, file_view, open_view

router = routers.DefaultRouter()
router.register('upload', UploadViewSet)

urlpatterns = [
    path('open', open_view),
    path('<str:token>', file_view),
    path('', include(router.urls))
]
