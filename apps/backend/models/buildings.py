from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Building(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"), db_index=True)
    description = models.TextField(
        blank=True, null=True, verbose_name=_("Description"), db_index=True
    )
    image = models.ImageField(
        db_index=True, verbose_name=_("Image"), upload_to="building/"
    )

    class Meta:
        verbose_name = _("Building")
        verbose_name_plural = _("Buildings")
        ordering = ("-created_at",)
        db_table = "building"

    def __str__(self):
        return self.title


class BuildingGallery(AbstractBaseModel):
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="gallery", db_index=True
    )
    image = models.ImageField(
        upload_to="building/gallery/", verbose_name=_("Image"), db_index=True
    )

    class Meta:
        verbose_name = _("Building Gallery")
        verbose_name_plural = _("Building Galleries")
        ordering = ("-created_at",)
        db_table = "building_gallery"

    def __str__(self):
        return self.building.title
