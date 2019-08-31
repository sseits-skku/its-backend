from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet as mvs
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)

from .models import Category, Tag, Comment, PostStatus, Post
from .serializers import (
    CategorySerializer, TagSerializer, CommentSerializer,
    PostSerializer, PostStatusSerializer
)
from utils.permissions import (
    IsOwner, IsStaffUser
)


class CategoryViewSet(mvs):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        perm_classes = [IsStaffUser]
        if self.action in ['list', 'retrieve']:
            perm_classes = [AllowAny]
        return [perm() for perm in perm_classes]


class TagViewSet(mvs):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        perm_classes = [IsStaffUser]
        if self.action in ['create', 'list', 'retrieve']:
            perm_classes = [AllowAny]
        return [perm() for perm in perm_classes]


class CommentAdminViewSet(mvs):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsStaffUser]


class CommentViewSet(mvs):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        p = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().get_queryset().filter(pk__in=p.comments.all())

    def get_permissions(self):
        member_zone = Category.objects.filter(member_only=True).all()
        p = get_object_or_404(Post, pk=self.kwargs['post_id'])
        perm_classes = [IsStaffUser]
        if self.action in ['retrieve']:
            if p.category not in member_zone and not p.deleted:
                perm_classes = [AllowAny]
        elif self.action in ['create']:
            if p.category not in member_zone and not p.deleted:
                perm_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            if p.category not in member_zone and not p.deleted:
                perm_classes = [IsOwner]
        return [perm() for perm in perm_classes]


class PostViewSet(mvs):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        c = get_object_or_404(Category, title=self.kwargs['category'])
        return super().get_queryset().filter(category=c.id)

    def get_permissions(self):
        member_zone = Category.objects.filter(member_only=True)
        perm_classes = [IsStaffUser]
        if self.action in ['retrieve', 'list']:
            if self.kwargs['category'] not in member_zone:
                perm_classes = [AllowAny]
        elif self.action in ['create']:
            if self.kwargs['category'] not in member_zone:
                perm_classes = [IsAuthenticated]
        elif self.kwargs['category'] not in member_zone:
            perm_classes = [IsOwner]
        return [perm() for perm in perm_classes]


class PostStatusViewSet(mvs):
    queryset = PostStatus.objects.all()
    serializer_class = PostStatusSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            perm_classes = [AllowAny]
        else:
            perm_classes = [IsStaffUser]
        return [perm() for perm in perm_classes]
