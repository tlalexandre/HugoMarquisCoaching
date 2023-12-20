from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from datetime import timedelta
from django.db.models import Q
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from .utils import check_overlap

# Create your models here.
DAYS_OF_WEEK = [
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
]
OPTIONS = ((0, _("Strength")), (1, _("Running")), (2, _("Stretch")))
LOCATION_CHOICES = [
    ("location1", _("Salle de sport(partenaire)")),
    ("location2", _("A domicile")),
    ("location3", _("En extérieur")),
    ("location4", _("Autre")),
]


class UnavailablePeriod(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="unavailable_periods"
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    slug = models.SlugField(max_length=255)

    def clean(self):
        # Check if there is any UnavailablePeriod that overlaps with this one
        overlapping_periods = UnavailablePeriod.objects.filter(
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        )
        if self.pk:
            overlapping_periods = overlapping_periods.exclude(pk=self.pk)
        if overlapping_periods.exists():
            raise ValidationError(
                "There is already an UnavailablePeriod in this time range."
            )

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.start_time}-{self.end_time}")
        self.clean()
        return super().save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_recurrent = models.BooleanField(default=False)
    day_of_week = models.IntegerField(
        choices=DAYS_OF_WEEK, null=True, blank=True)
    type = models.IntegerField(choices=OPTIONS, default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses_created"
    )
    participants = models.ManyToManyField(User, related_name="courses_joined")
    max_participants = models.IntegerField()
    location = models.TextField()

    def add_participant(self, user):
        if self.participants.count() < self.max_participants:
            self.participants.add(user)
            self.save()
        else:
            raise ValidationError("This course is full")

    def remove_participant(self):
        if self.participants > 0:
            self.participants -= 1
            self.save()
        else:
            raise ValidationError("There are no participants to remove.")

    def hours(self, end_time, start_time):
        if end_time < start_time:
            raise ValidationError(
                "End time must be greater than or equal to start time"
            )
        return self.end_time - self.start_time

    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is not in the database yet
            super().save(*args, **kwargs)  # Save it to get an ID

        self.slug = slugify(f"{self.name}-{self.pk}")

        if self._state.adding:
            if check_overlap(
                self.start_time, self.end_time, Course, self.pk
            ) or check_overlap(self.start_time, self.end_time, PrivateSession):
                raise ValidationError(
                    "Another event already exists within this time range."
                )

        super().save(*args, **kwargs)


class PrivateSession(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=OPTIONS, default=0)
    location = models.CharField(max_length=255, choices=LOCATION_CHOICES)
    is_approved = models.BooleanField(default=False)

    def is_creator(self, user):
        return self.user == user

    def hours(self, end_time, start_time):
        if end_time < start_time:
            raise ValidationError(
                "End time must be greater than or equal to start time"
            )
        return self.end_time - self.start_time

    def clean(self):
        super().clean()
        duration = self.end_time - self.start_time
        if duration > timedelta(hours=1):
            raise ValidationError(
                "The duration of a private session cannot exceed one hour."
            )

    def approve(self):
        self.is_approved = True
        super().save(force_update=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is not in the database yet
            super().save(*args, **kwargs)  # Save it to get an ID

        self.slug = slugify(f"{self.name}-{self.pk}")

        if self._state.adding:
            if (
                check_overlap(self.start_time, self.end_time, Course)
                or check_overlap(
                    self.start_time, self.end_time, PrivateSession, self.pk
                )
                or check_overlap(
                    self.start_time, self.end_time, UnavailablePeriod)
            ):
                raise ValidationError(
                    "Another event already exists within this time range."
                )

        super().save(*args, **kwargs)
