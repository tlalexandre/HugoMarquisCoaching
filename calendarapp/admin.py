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

