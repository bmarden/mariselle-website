from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

# View to register a new user


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        # Check if the form submitted is valid
        if form.is_valid():
            # Save form
            form.save()
            username = form.cleaned_data.get("username")
            # Create a message that the account has been created
            messages.success(request, f"Account Created! Login Here")
            return redirect("login")

        # If method is not POST then display the empty registration form
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


# Require login to access profile view
@login_required
def profile(request):
    if request.method == "POST":
        # Populate user update form with the current user's information
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # Populate the profile form with the user's profile information
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        # If both forms are valid then save and create an account updated message
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")  # Redirects back to profile page
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "users/profile.html", context)
