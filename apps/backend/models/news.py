from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class NewsCategory(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), db_index=True)

    class Meta:
        verbose_name = _("News Category")
        verbose_name_plural = _("News Categories")
        ordering = ("name",)
        db_table = "news_category"

    def __str__(self):
        return self.name


class News(AbstractBaseModel):
    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        db_index=True,
    )
    title = models.CharField(max_length=255, verbose_name=_("Title"), db_index=True)
    description = models.TextField(verbose_name=_("Description"), db_index=True)
    image = models.ImageField(upload_to="news/", verbose_name=_("Image"), db_index=True)

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ("-created_at",)
        db_table = "news"

    def __str__(self):
        return self.title
