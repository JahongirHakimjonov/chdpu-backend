from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.backend.forms.interview import InterviewForm
from apps.backend.models.interview import Interview


@admin.register(Interview)
class InterviewAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    form = InterviewForm
