from rest_framework.serializers import ModelSerializer as ms

from .models import Category, Tag, Comment, Post, PostStatus


class CategorySerializer(ms):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(ms):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(ms):
    class Meta:
        model = Comment
        fields = '__all__'


class PostStatusSerializer(ms):
    class Meta:
        model = PostStatus
        fields = '__all__'


class PostSerializer(ms):
    class Meta:
        model = Post
        fields = '__all__'
