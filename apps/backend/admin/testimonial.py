from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.backend.models.testimonial import Testimonial


@admin.register(Testimonial)
class Testimonial(ModelAdmin):
    list_display = ("name", "chair", "created_at", "updated_at")
    search_fields = ("name", "chair__name")
    list_filter = ("chair",)
    autocomplete_fields = ("chair",)
