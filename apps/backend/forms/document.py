from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.document import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
