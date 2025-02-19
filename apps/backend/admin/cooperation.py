from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.models.cooperation import Cooperation


@admin.register(Cooperation)
class CooperationAdmin(ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
