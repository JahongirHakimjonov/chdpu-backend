from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.models.laboratory import Laboratory


@admin.register(Laboratory)
class LaboratoryAdmin(ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
