from django.contrib import admin

from .models import OHTable


@admin.register(OHTable)
class OHTableAdmin(admin.ModelAdmin):
    pass
