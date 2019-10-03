from django.contrib import admin

from .models import OHTable, OHEntry


@admin.register(OHTable)
class OHTableAdmin(admin.ModelAdmin):
    pass


@admin.register(OHEntry)
class OHEntryAdmin(admin.ModelAdmin):
    pass
