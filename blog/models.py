from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """ Model for blog posts  """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField("image", default="placeholder")
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # save the object to generate an ID
        if not self.slug:  # if the slug is not set
            # generate a slug using the title and ID
            self.slug = slugify(f"{self.title}-{self.id}")
            super().save(*args, **kwargs)


class Comment(models.Model):
    """ Model for blog comments """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
