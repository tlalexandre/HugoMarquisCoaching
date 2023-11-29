from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

OPTIONS = ((0, "Strength"), (1, "Running"), (2, "Stretch"))

class UnavailablePeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='unavailable_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    slug = models.SlugField(max_length=255)

    def clean(self):
        # Check if there is any UnavailablePeriod that overlaps with this one
        overlapping_periods = UnavailablePeriod.objects.filter(
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        )
        if self.pk:  # If this is an existing instance, exclude it from the query
            overlapping_periods = overlapping_periods.exclude(pk=self.pk)
        if overlapping_periods.exists():
            raise ValidationError('There is already an UnavailablePeriod in this time range.')

    def save(self, *args, **kwargs):
        self.slug= slugify(f'{self.start_time}-{self.end_time}')
        self.clean()
        return super().save(*args, **kwargs)

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    type=models.IntegerField(choices=OPTIONS, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_created')
    participants = models.ManyToManyField(User, related_name='courses_joined')
    max_participants = models.IntegerField()
    location = models.TextField()

    def add_participant(self,user):
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
            
    def hours(self):
        if end_time < start_time:
            raise ValidationError(
                "End time must be greater than or equal to start time"
            )
        return self.end_time - self.start_time

    def save(self, *args, **kwargs):
        overlapping_courses = Course.objects.filter(
            user=self.user,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(pk=self.pk)  # Exclude the current instance if it's being updated

        overlapping_private_sessions = PrivateSession.objects.filter(
            user=self.user,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        )

        if overlapping_courses.exists() or overlapping_private_sessions.exists():
            raise ValidationError("Another event already exists within this time range.")

        super().save(*args, **kwargs)

class PrivateSession(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=OPTIONS, default=0)
    location = models.TextField()
    
    def is_creator(self, user):
        return self.user == user

    def hours(self):
        if end_time < start_time:
            raise ValidationError(
                "End time must be greater than or equal to start time"
            )
        return self.end_time - self.start_time

    def save(self, *args, **kwargs):
        overlapping_courses = Course.objects.filter(
            user=self.user,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        ).exclude(pk=self.pk)  # Exclude the current instance if it's being updated

        overlapping_private_sessions = PrivateSession.objects.filter(
            user=self.user,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
        )

        if overlapping_courses.exists() or overlapping_private_sessions.exists():
            raise ValidationError("Another event already exists within this time range.")

        superuser = User.objects.get(is_superuser=True)
        if UnavailablePeriod.objects.filter(user=superuser, start_time__lt=self.end_time, end_time__gt=self.start_time).exists():
            raise ValidationError("The superuser is not available during this session time")

        super().save(*args, **kwargs)
