from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.models.leadership import Leadership


@admin.register(Leadership)
class LeadershipAdmin(ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
