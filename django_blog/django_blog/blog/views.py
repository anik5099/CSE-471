from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Post


def signup(request):
    if request.method == "POST":
        username = request.POST.get("uname", "").strip()
        email = request.POST.get("uemail", "").strip()
        password = request.POST.get("upassword", "")

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect("signup-page")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another username.")
            return redirect("signup-page")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully. Please login.")
        return redirect("login-page")

    return render(request, "blog/signup.html")


def loginn(request):
    if request.method == "POST":
        username = request.POST.get("uname", "").strip()
        password = request.POST.get("upassword", "")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home-page")

        messages.error(request, "Invalid username or password.")
        return redirect("login-page")

    return render(request, "blog/loginn.html")


@login_required(login_url="login-page")
def home(request):
    context = {
        "posts": Post.objects.all().order_by("-date_posted")
    }
    return render(request, "blog/home.html", context)


@login_required(login_url="login-page")
def newPost(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if not title or not content:
            messages.error(request, "Title and content are required.")
            return redirect("new-post")

        Post.objects.create(title=title, content=content, author=request.user)
        messages.success(request, "Post created successfully.")
        return redirect("home-page")

    return render(request, "blog/newpost.html")


@login_required(login_url="login-page")
def myPost(request):
    context = {
        "posts": Post.objects.filter(author=request.user).order_by("-date_posted")
    }
    return render(request, "blog/mypost.html", context)


def signout(request):
    logout(request)
    return redirect("login-page")
