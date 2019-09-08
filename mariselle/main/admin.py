from django.contrib import admin
from .models import Picture, HomePicture, Post, Comment

# Register your models here.

admin.site.register(Picture)
admin.site.register(HomePicture)
admin.site.register(Post)
admin.site.register(Comment)
