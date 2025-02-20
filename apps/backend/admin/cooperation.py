from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.backend.forms.cooperation import CooperationForm
from apps.backend.models.cooperation import Cooperation


@admin.register(Cooperation)
class CooperationAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    form = CooperationForm
