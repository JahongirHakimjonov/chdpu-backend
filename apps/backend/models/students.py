from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Student(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"), db_index=True)
    description = models.TextField(verbose_name=_("Description"), db_index=True)
    image = models.ImageField(upload_to="news/", verbose_name=_("Image"), db_index=True)

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
        ordering = ("-created_at",)
        db_table = "student"

    def __str__(self):
        return self.title
