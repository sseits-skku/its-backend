from django.contrib import admin

from .models import Apply


@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    pass
