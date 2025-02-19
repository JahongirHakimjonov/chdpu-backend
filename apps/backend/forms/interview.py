from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.interview import Interview


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
