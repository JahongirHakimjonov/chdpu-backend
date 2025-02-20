from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.backend.forms.laboratory import LaboratoryForm
from apps.backend.models.laboratory import Laboratory


@admin.register(Laboratory)
class LaboratoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    form = LaboratoryForm
