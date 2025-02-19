from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.cooperation import Cooperation


class CooperationForm(forms.ModelForm):
    class Meta:
        model = Cooperation
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
