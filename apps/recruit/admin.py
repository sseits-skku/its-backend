from django.contrib import admin

from .models import ApplyTerm, Apply


@admin.register(ApplyTerm)
class ApplyTermAdmin(admin.ModelAdmin):
    pass


@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    pass
