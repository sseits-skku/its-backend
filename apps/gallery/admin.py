from django.contrib import admin

from .models import Gallery, Image


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
