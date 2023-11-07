from django.contrib import admin
from .models import Coach, Course, PrivateSession, Availability


# Register your models here.
@admin.register(Coach)
class Coach(admin.ModelAdmin):
    list_display = ("name", "email", "phone")


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "start_time",
        "end_time",
        "coach",
        "user",
        "max_participants",
        "actual_participants",
        "location",
    )


@admin.register(PrivateSession)
class PrivateSession(admin.ModelAdmin):
    list_display = (
        "coach",
        "start_time",
        "end_time",
        "day_of_the_week",
        "user",
        "description",
    )


@admin.register(Availability)
class Availability(admin.ModelAdmin):
    list_display = (
        "coach",
        "start_time",
        "end_time",
        "day_of_the_week",
        "is_available",
    )
