from django.contrib import admin
from django.db import models
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from unfold.admin import ModelAdmin, StackedInline
from unfold.contrib.forms.widgets import WysiwygWidget

from apps.backend.models.chair import Chair, ChairMember


class ChairMemberInline(StackedInline, TranslationStackedInline):
    model = ChairMember
    extra = 0
    fields = ("name", "title", "description", "image")
    # form = ChairMemberForm
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
    # form = ChairForm
    inlines = (ChairMemberInline,)
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
