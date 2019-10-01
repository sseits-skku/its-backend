from django.contrib import admin

from .models import Choice, BasePoll


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(BasePoll)
class BasePollAdmin(admin.ModelAdmin):
    pass
