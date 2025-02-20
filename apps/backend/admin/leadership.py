from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.backend.forms.leadership import LeadershipForm
from apps.backend.models.leadership import Leadership


@admin.register(Leadership)
class LeadershipAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    form = LeadershipForm
