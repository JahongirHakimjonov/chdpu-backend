from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from apps.backend.models.chair import Chair, ChairMember


class ChairForm(forms.ModelForm):
    class Meta:
        model = Chair
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }


class ChairMemberForm(forms.ModelForm):
    class Meta:
        model = ChairMember
        fields = "__all__"
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"},
            )
        }
