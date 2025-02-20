from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.backend.forms.chair import ChairForm
from apps.backend.models.chair import Chair


@admin.register(Chair)
class ChairAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    form = ChairForm
