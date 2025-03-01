from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Document(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255, db_index=True)
    description = models.TextField(
        verbose_name=_("Description"), blank=True, null=True, db_index=True
    )
    image = models.ImageField(
        upload_to="document/", verbose_name=_("Image"), db_index=True
    )

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")
        ordering = ("-created_at",)
        db_table = "document"

    def __str__(self):
        return self.title
