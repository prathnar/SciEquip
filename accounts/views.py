from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "Signup successful! Please login.")
            return redirect("login")

    return render(request, "accounts/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}")
            return redirect("view_cart")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")
