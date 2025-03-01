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


class InfoContact(AbstractBaseModel):
    class ContactType(models.TextChoices):
        EMAIL = "EMAIL", _("Email")
        PHONE = "PHONE", _("Phone")
        TELEGRAM = "TELEGRAM", _("Telegram")
        FACEBOOK = "FACEBOOK", _("Facebook")
        INSTAGRAM = "INSTAGRAM", _("Instagram")
        TWITTER = "TWITTER", _("Twitter")
        LINKEDIN = "LINKEDIN", _("LinkedIn")
        WEBSITE = "WEBSITE", _("Website")
        YOUTUBE = "YOUTUBE", _("YouTube")
        OTHER = "OTHER", _("Other")

    info = models.ForeignKey(
        "Info",
        on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name=_("Info"),
        db_index=True,
    )
    value = models.CharField(max_length=255, verbose_name=_("Value"), db_index=True)
    contact_type = models.CharField(
        max_length=255,
        choices=ContactType,
        verbose_name=_("Contact Type"),
        db_index=True,
    )

    class Meta:
        verbose_name = _("Info Contact")
        verbose_name_plural = _("Info Contacts")
        ordering = ("-created_at",)
        db_table = "info_contact"

    def __str__(self):
        return self.value
