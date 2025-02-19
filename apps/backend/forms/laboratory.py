from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.laboratory import Laboratory


class LaboratoryForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
