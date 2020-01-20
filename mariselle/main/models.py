from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Model for gallery images
class Picture(models.Model):
    title = models.TextField()
    img = models.ImageField(upload_to="gallery_images/")

    class Meta:
        permissions = (("patreon", "Patreon gallery access"),)

    # Return string for title
    def __str__(self):
        return self.title


# Model for images posted on the home page
class HomePicture(models.Model):
    title = models.TextField(max_length=250)
    description = models.TextField(default='')
    img = models.ImageField(upload_to="home_images/")

    # Return string for title
    def __str__(self):
        return self.title


class Post(models.Model):
    # Title of the post, max length of 250 chars
    title = models.CharField(max_length=250)
    # Content of the post
    content = models.TextField()
    # To hold the date the post was created
    date_posted = models.DateTimeField(default=timezone.now)
    # Image for the post
    img = models.ImageField(null=True, blank=True, upload_to="post_images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    # author information, User -> 1:M relationship
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Post information, Post -> 1:M relationship
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    # Content of the comment
    content = models.TextField(max_length=5000)
    # Hold the date posted
    date_posted = models.DateTimeField(default=timezone.now)
