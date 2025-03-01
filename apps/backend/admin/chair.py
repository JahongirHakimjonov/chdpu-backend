from django.contrib import admin
from django.db import models
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from unfold.contrib.forms.widgets import WysiwygWidget

from apps.backend.models.chair import Chair, ChairMember, ChairContact


class ChairContactInline(TabularInline):
    model = ChairContact
    extra = 0
    tab = True
    fields = ("contact_type", "value")


class ChairMemberInline(StackedInline, TranslationStackedInline):
    model = ChairMember
    extra = 0
    tab = True
    fields = ("name", "title", "description", "image")
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }


@admin.register(Chair)
class ChairAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")
    inlines = (ChairMemberInline, ChairContactInline)
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }


@admin.register(ChairMember)
class ChairMemberAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "chair", "created_at", "updated_at")
    search_fields = ("name", "chair__name")
    list_filter = ("chair",)
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    autocomplete_fields = ("chair",)
