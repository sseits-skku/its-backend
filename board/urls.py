from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, TagViewSet,    \
                   PostStatusViewSet, PostViewSet, \
                   CommentViewSet, CommentAdminViewSet

router = routers.DefaultRouter()
router.register('tag', TagViewSet)
router.register('category', CategoryViewSet)
router.register('post-status', PostStatusViewSet)
router.register('comment-admin', CommentAdminViewSet)
router2 = routers.DefaultRouter()
router2.register('', PostViewSet)
router3 = routers.DefaultRouter()
router3.register('', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('post/<str:category>/', include(router2.urls)),
    path('comment/<int:post_id>/', include(router3.urls))
]
