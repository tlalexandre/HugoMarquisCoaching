from django.contrib import admin
from .models import Course, PrivateSession





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
        "max_participants",
        "actual_participants",
        "location",
    )


@admin.register(PrivateSession)
class PrivateSession(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "name",
        "slug",
        "start_time",
        "end_time",
        "day_of_the_week",
        "user",
        "description",
    )

