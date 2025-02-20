from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin

from apps.backend.forms.students import StudentForm
from apps.backend.models.students import Student


@admin.register(Student)
class StudentAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    form = StudentForm
