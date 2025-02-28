from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, TabularInline

from apps.backend.forms.laboratory import LaboratoryForm
from apps.backend.models.laboratory import Laboratory, LaboratoryGallery


class LaboratoryGalleryInline(TabularInline):
    model = LaboratoryGallery
    extra = 0
    fields = ("image",)


@admin.register(Laboratory)
class LaboratoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    form = LaboratoryForm
    inlines = (LaboratoryGalleryInline,)


@admin.register(LaboratoryGallery)
class LaboratoryGalleryAdmin(ModelAdmin):
    list_display = ("id", "laboratory", "created_at", "updated_at")
    search_fields = ("laboratory__title",)
    list_filter = ("created_at", "updated_at")
    autocomplete_fields = ("laboratory",)
