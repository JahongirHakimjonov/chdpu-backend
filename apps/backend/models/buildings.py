from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Building(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    image = models.ImageField()

    class Meta:
        verbose_name = _("Building")
        verbose_name_plural = _("Buildings")

    def __str__(self):
        return self.title


class BuildingGallery(AbstractBaseModel):
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="gallery"
    )
    image = models.ImageField()

    class Meta:
        verbose_name = _("Building Gallery")
        verbose_name_plural = _("Building Galleries")

    def __str__(self):
        return self.building.title
