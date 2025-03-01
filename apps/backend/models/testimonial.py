from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Testimonial(AbstractBaseModel):
    chair = models.ForeignKey(
        "Chair",
        on_delete=models.CASCADE,
        related_name="testimonials",
        verbose_name=_("Chair"),
        db_index=True,
    )
    name = models.CharField(max_length=255, verbose_name=_("Name"), db_index=True)
    content = models.TextField(verbose_name=_("Content"), db_index=True)
    image = models.ImageField(
        upload_to="testimonial/", verbose_name=_("Image"), db_index=True
    )

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")
        ordering = ("-created_at",)
        db_table = "testimonial"

    def __str__(self):
        return self.name
