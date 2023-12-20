from django.contrib import admin
from .models import Course, PrivateSession, UnavailablePeriod


@admin.register(Course)
class Course(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "name",
        "slug",
        "description",
        "start_time",
        "end_time",
        "user",
        "type",
        "max_participants",
        "location",
        "id",
    )


@admin.register(PrivateSession)
class PrivateSession(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "name",
        "slug",
        "start_time",
        "end_time",
        "user",
        "location",
        "type",
    )


@admin.register(UnavailablePeriod)
class UnavailablePeriod(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("start_time", "end_time")}
    list_display = (
        "slug",
        "start_time",
        "end_time",
        "user",
    )
