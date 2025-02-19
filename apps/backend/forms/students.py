from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.students import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
