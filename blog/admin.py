from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("status", "created_on")
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ("title", "content")
    summernote_fields = "content"


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on")
    search_fields = ("name", "email", "body")
