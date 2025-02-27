from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class NewsCategory(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("News Category")
        verbose_name_plural = _("News Categories")
        ordering = ("name",)

    def __str__(self):
        return self.name


class News(AbstractBaseModel):
    category = models.ForeignKey(
        NewsCategory, on_delete=models.CASCADE, verbose_name=_("Category")
    )
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to="news/", verbose_name=_("Image"))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
