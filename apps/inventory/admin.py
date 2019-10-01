from django.contrib import admin

from .models import Place, Status, OSType, Stock, ComputerStock


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(OSType)
class OSTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass


@admin.register(ComputerStock)
class ComputerStockAdmin(admin.ModelAdmin):
    pass
