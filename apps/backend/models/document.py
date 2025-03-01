from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Document(AbstractBaseModel):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True,
    )
    image = models.ImageField()

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")

    def __str__(self):
        return self.title
