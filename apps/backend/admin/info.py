from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, TabularInline

from apps.backend.forms.info import InfoForm
from apps.backend.models.info import Info, InfoContact


class ChairContactInline(TabularInline):
    model = InfoContact
    extra = 0
    tab = True
    fields = ("contact_type", "value")


@admin.register(Info)
class InfoAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "updated_at")
    form = InfoForm
    inlines = (ChairContactInline,)
