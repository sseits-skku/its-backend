from django.contrib import admin
from .models import ImageContent, FileContent


@admin.register(ImageContent)
class ImageContentAdmin(admin.ModelAdmin):
    pass


@admin.register(FileContent)
class FileContentAdmin(admin.ModelAdmin):
    pass
