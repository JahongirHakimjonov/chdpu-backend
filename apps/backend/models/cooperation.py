from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Cooperation(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to="cooperation/", verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Cooperation")
        verbose_name_plural = _("Cooperations")
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
