from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail

# Some class view imports
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from . import models
from .models import Picture, HomePicture, Post, Comment
from .forms import BookingForm

# Create your views here.

# Default home view
def home(request):
    context = {
        "posts": models.Post.objects.all().order_by("-date_posted")[:3],
        "title": "Lala Mariselle Home",
        "pic_list": models.HomePicture.objects.all(),
    }
    return render(request, "main/home.html", context=context)


class PostView(ListView):
    # Set model equal to Post object
    model = Post
    # Set the template to use
    template_name = "main/home.html"
    # Set the name of the object
    context_object_name = "posts"
    # Set ordering, newest first
    ordering = ["-date_posted"]


class PostDetail(DetailView):
    model = Post


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):

    model = Post
    fields = ["title", "content"]

    def test_func(self):
        post = self.get_object()

        if post.UserPassesTestMixin(lambda u: u.is_superuser):
            return True
        return False

    def form_valid(self, form):
        return super().form_valid(form)


# View for gallery images. Located on the gallery page


@permission_required("main.patreon")
def gallery(request):
    pic_list = models.Picture.objects.all()
    # Display 10 images before paginating to next page
    paginator = Paginator(pic_list, 10)

    # Setup how paginator works
    page = request.GET.get("page")
    pics = paginator.get_page(page)
    return render(request, "main/gallery.html", {"pics": pics})


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email, ["benmarden@outlook.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            messages.success(request, f"Message successfully sent!")
            return redirect("home")

    else:
        form = BookingForm(request.POST)

    return render(request, "main/booking.html", {"form": form})


def about(request):
    context = {"title": "About Lala Mariselle"}
    return render(request, "main/about.html", context)

