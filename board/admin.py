from django.contrib import admin
from .models import Category, Tag, Post, \
                    PostStatus, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_type', 'category']


@admin.register(PostStatus)
class PostStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
    """
    def name(instance):
        return instance.last_name+instance.first_name

    name.short_description = '이름'

    list_display = ['id', 'username', 'nickname',
                    'date_joined', name, 'email',
                    'last_login', 'is_active', 'is_staff',
                    'is_superuser']
    list_display_links = ['id', name]
    list_editable = ['is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_active', 'is_staff']
    search_fields = ['id', 'username', 'email', 'nickname', name]
    fieldsets = [
        ('기본 정보', {
            'fields': ('username', 'nickname', 'first_name',
                       'last_name', 'email', 'password')
        }),
        ('권한 설정', {
            'fields': ('is_staff', 'is_superuser',)
        }),
        ('상태 설정', {
            'fields': ('is_active',)
        }),
    ]
    """
