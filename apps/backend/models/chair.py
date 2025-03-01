from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Chair(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to="chair/", verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Chair")
        verbose_name_plural = _("Chairs")
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class ChairMember(AbstractBaseModel):
    chair = models.ForeignKey(
        "Chair",
        on_delete=models.CASCADE,
        related_name="members",
        verbose_name=_("Chair"),
    )
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to="chair/member/", verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Chair Member")
        verbose_name_plural = _("Chair Members")
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class ChairContact(AbstractBaseModel):
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

    chair = models.ForeignKey(
        "Chair",
        on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name=_("Chair"),
    )
    value = models.CharField(max_length=255, verbose_name=_("Value"))
    contact_type = models.CharField(
        max_length=255, choices=ContactType, verbose_name=_("Contact Type")
    )

    class Meta:
        verbose_name = _("Chair Contact")
        verbose_name_plural = _("Chair Contacts")
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
