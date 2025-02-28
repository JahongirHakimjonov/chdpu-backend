from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Leadership(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    sub_title = models.CharField(max_length=255, verbose_name=_("Sub Title"))
    description = models.TextField(verbose_name=_("Description"))
    contact = models.CharField(max_length=255, verbose_name=_("Contact"))
    image = models.ImageField(upload_to="leadership/", verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Leadership")
        verbose_name_plural = _("Leaderships")
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class WorkTimeline(AbstractBaseModel):
    class WeekDay(models.TextChoices):
        MONDAY = "Monday", _("Monday")
        TUESDAY = "Tuesday", _("Tuesday")
        WEDNESDAY = "Wednesday", _("Wednesday")
        THURSDAY = "Thursday", _("Thursday")
        FRIDAY = "Friday", _("Friday")
        SATURDAY = "Saturday", _("Saturday")
        SUNDAY = "Sunday", _("Sunday")

    leadership = models.ForeignKey(
        "Leadership",
        on_delete=models.CASCADE,
        related_name="work_timelines",
        verbose_name=_("Leadership"),
    )
    day = models.CharField(max_length=255, choices=WeekDay, verbose_name=_("Day"))
    start_time = models.TimeField(verbose_name=_("Start Time"))
    end_time = models.TimeField(verbose_name=_("End Time"))
