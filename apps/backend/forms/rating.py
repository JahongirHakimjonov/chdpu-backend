from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.rating import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
