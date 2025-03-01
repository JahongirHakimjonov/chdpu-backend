from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Chair(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"), db_index=True)
    title = models.CharField(max_length=255, verbose_name=_("Title"), db_index=True)
    description = models.TextField(verbose_name=_("Description"), db_index=True)
    image = models.ImageField(
        upload_to="chair/", verbose_name=_("Image"), db_index=True
    )

    class Meta:
        verbose_name = _("Chair")
        verbose_name_plural = _("Chairs")
        ordering = ("-created_at",)
        db_table = "chair"

    def __str__(self):
        return self.name


class ChairMember(AbstractBaseModel):
    chair = models.ForeignKey(
        "Chair",
        on_delete=models.CASCADE,
        related_name="members",
        verbose_name=_("Chair"),
        db_index=True,
    )
    name = models.CharField(max_length=255, verbose_name=_("Name"), db_index=True)
    title = models.CharField(max_length=255, verbose_name=_("Title"), db_index=True)
    description = models.TextField(verbose_name=_("Description"), db_index=True)
    image = models.ImageField(
        upload_to="chair/member/", verbose_name=_("Image"), db_index=True
    )
    position = models.BigIntegerField(
        verbose_name=_("Position"), db_index=True, default=0
    )

    class Meta:
        verbose_name = _("Chair Member")
        verbose_name_plural = _("Chair Members")
        ordering = ["position"]
        db_table = "chair_member"

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
        verbose_name = _("Chair Contact")
        verbose_name_plural = _("Chair Contacts")
        ordering = ("-created_at",)
        db_table = "chair_contact"

    def __str__(self):
        return self.value
