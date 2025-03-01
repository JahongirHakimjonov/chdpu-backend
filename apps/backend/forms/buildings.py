from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.buildings import Building


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
