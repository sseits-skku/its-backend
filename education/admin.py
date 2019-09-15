from django.contrib import admin

from .models import Category, Education


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass
