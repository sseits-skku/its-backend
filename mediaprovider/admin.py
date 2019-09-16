from django.contrib import admin

from .models import FileModel


@admin.register(FileModel)
class FileAdmin(admin.ModelAdmin):
    fieldsets = [('파일 업로드', {'fields': ('file', 'is_public')})]
