from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.leadership import Leadership


class LeadershipForm(forms.ModelForm):
    class Meta:
        model = Leadership
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
