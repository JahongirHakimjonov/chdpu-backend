from typing import Any

from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from unfold.contrib.filters.admin import DropdownFilter
from unfold.contrib.forms.widgets import WysiwygWidget

from apps.backend.models.chair import Chair, ChairMember, ChairContact


class ChairFilter(DropdownFilter):
    title = _("Chair")
    parameter_name = "chair"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        querysets = Chair.objects.all()
        return [
            (queryset.id, f"{queryset.name} - {queryset.title}")
            for queryset in querysets
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value():
            return queryset.filter(chair_id__id=self.value())
        return queryset


class ChairContactInline(TabularInline):
    model = ChairContact
    extra = 0
    tab = True
    fields = ("contact_type", "value")


class ChairMemberInline(StackedInline, TranslationStackedInline):
    model = ChairMember
    extra = 0
    tab = True
    fields = ("name", "title", "description", "image", "position")
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
class ChairMemberAdmin(SortableAdminMixin, ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "name", "chair", "created_at", "position")
    search_fields = ("name", "chair__name")
    list_filter = (ChairFilter, "created_at")
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    ordering = ("position",)
    autocomplete_fields = ("chair",)


@admin.register(ChairContact)
class ChairContactAdmin(ModelAdmin):
    list_display = ("id", "chair", "contact_type", "value", "created_at")
    search_fields = ("chair__title", "contact_type", "value")
    list_filter = ("chair", "contact_type")
    autocomplete_fields = ("chair",)
