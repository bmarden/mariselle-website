from django.urls import path
from .views import PostView, PostDetail, PostCreate
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post-detail"),
    # path("post/<int:pk>/update/", PostUpdate.as_view(), name="post-update"),
    # path("post/<int:pk>/delete/", PostDelete.as_view(), name="post-delete"),
    path("post/new/", PostCreate.as_view(), name="post-create"),
    path("gallery/", views.gallery, name="gallery"),
    path("booking/", views.booking, name="booking"),
    path("about/", views.about, name="about"),
]

