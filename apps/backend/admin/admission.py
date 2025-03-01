from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.backend.forms.admission import AdmissionForm
from apps.backend.models.admission import Admission


@admin.register(Admission)
class AdmissionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    form = AdmissionForm
