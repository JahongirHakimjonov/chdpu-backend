from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.news import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
