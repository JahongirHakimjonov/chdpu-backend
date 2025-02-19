from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.models.info import Info


@admin.register(Info)
class InfoAdmin(ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "updated_at")
