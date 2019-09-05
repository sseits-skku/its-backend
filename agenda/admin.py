from django.contrib import admin
from .models import Agenda, Action, Label


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    pass


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    pass
