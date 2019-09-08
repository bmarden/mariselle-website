from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    # Create 1:1 mapping of a User to a profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        # Print user name
        return f"{self.user.username} Profile"

    def save(self, *args, **kawrgs):
        # Override the save method to resize profile images
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)

        # Check if the image is too large
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)

            # Save new image size
            img.thumbnail(output_size)
            img.save(self.image.path)

