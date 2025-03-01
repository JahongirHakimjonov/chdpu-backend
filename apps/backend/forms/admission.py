from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.admission import Admission


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
