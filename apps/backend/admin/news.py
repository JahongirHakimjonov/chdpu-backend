from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.forms.news import NewsForm
from apps.backend.models.news import News


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    form = NewsForm
