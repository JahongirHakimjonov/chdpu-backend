from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, TabularInline

from apps.backend.forms.leadership import LeadershipForm
from apps.backend.models.leadership import Leadership, WorkTimeline


class WorkTimelineInline(TabularInline):
    model = WorkTimeline
    extra = 0
    fields = ("day", "start_time", "end_time")


@admin.register(Leadership)
class LeadershipAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    form = LeadershipForm
    inlines = (WorkTimelineInline,)


@admin.register(WorkTimeline)
class WorkTimelineAdmin(ModelAdmin):
    list_display = ("id", "day", "start_time", "end_time")
    search_fields = ("day",)
    list_filter = ("day",)
    autocomplete_fields = ("leadership",)
