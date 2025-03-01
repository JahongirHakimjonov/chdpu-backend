from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, TabularInline

from apps.backend.forms.buildings import BuildingForm
from apps.backend.models.buildings import Building, BuildingGallery


class BuildingGalleryInline(TabularInline):
    model = BuildingGallery
    extra = 0


@admin.register(BuildingGallery)
class BuildingGalleryAdmin(ModelAdmin):
    list_display = ("id", "building", "created_at")
    search_fields = ("building__title",)
    list_filter = ("created_at",)
    autocomplete_fields = ("building",)


@admin.register(Building)
class BuildingAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    form = BuildingForm
    inlines = (BuildingGalleryInline,)
