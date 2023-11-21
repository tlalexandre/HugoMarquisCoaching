from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


# class CalendarEvent(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     date = models.DateField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     start_hour = models.TimeField()
#     end_hour = models.TimeField()
#     is_available = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.date} - {self.hour} - {self.user.username}"

OPTIONS = ((0, "Strength"), (1, "Running"), (2, "Stretch"))


# class Coach(models.Model):
#     name = models.CharField(max_length=200, unique=True)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         return self.name

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    day_of_the_week = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    max_participants = models.IntegerField()
    actual_participants = models.IntegerField()
    location = models.TextField()

    def __str__(self):
        return self.name

class PrivateSession(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    day_of_the_week = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.IntegerField(choices=OPTIONS, default=0)
    

# class Availability(models.Model):
#     coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     day_of_the_week = models.DateTimeField()
#     is_available = models.BooleanField()

#     def clean(self):
#         if self.end_time < self.start_time:
#             raise ValidationError(
#                 "End time must be greater than or equal to start time"
#             )

#     def __str__(self):
#         return f"{self.coach.name}'s Availability from {self.start_time} to {self.end_time}"
