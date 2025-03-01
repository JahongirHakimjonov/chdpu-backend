from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Info(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"), db_index=True)
    description = models.TextField(verbose_name=_("Description"), db_index=True)
    image = models.ImageField(upload_to="info/", verbose_name=_("Image"), db_index=True)

    class Meta:
        verbose_name = _("Info")
        verbose_name_plural = _("Infos")
        ordering = ("-created_at",)
        db_table = "info"

    def __str__(self):
        return self.title
