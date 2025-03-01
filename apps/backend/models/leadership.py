from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models.base import AbstractBaseModel


class Leadership(AbstractBaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"), db_index=True)
    sub_title = models.CharField(
        max_length=255, verbose_name=_("Sub Title"), db_index=True
    )
    description = models.TextField(verbose_name=_("Description"), db_index=True)
    contact = models.CharField(max_length=255, verbose_name=_("Contact"), db_index=True)
    image = models.ImageField(
        upload_to="leadership/", verbose_name=_("Image"), db_index=True
    )
    position = models.BigIntegerField(
        verbose_name=_("Position"), db_index=True, default=0
    )

    class Meta:
        verbose_name = _("Leadership")
        verbose_name_plural = _("Leaderships")
        ordering = ("position",)
        db_table = "leadership"

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
        db_index=True,
    )
    day = models.CharField(
        max_length=255, choices=WeekDay, verbose_name=_("Day"), db_index=True
    )
    start_time = models.TimeField(verbose_name=_("Start Time"), db_index=True)
    end_time = models.TimeField(verbose_name=_("End Time"), db_index=True)

    class Meta:
        verbose_name = _("Work Timeline")
        verbose_name_plural = _("Work Timelines")
        ordering = ("-created_at",)
        db_table = "work_timeline"

    def __str__(self):
        return self.leadership.title
