from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.backend.forms.rating import RatingForm
from apps.backend.models.rating import Rating


@admin.register(Rating)
class RatingAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    form = RatingForm
