from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blogs.models import Blog

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("blogs:index"))


def register(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "users/register.html", {"form": form})

    elif request.method == "POST":
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            auth_user = authenticate(username=new_user.username, password=request.POST["password1"])
            login(request, auth_user)
            return HttpResponseRedirect("/")



def list_user(request):
    users = User.objects.all()
    return render(request, "users/list.html", {"users": users})


def user(request, user_id):
    user = User.objects.get(username=user_id)
    all_blogs = Blog.objects.all()
    blogs = []
    for blog in all_blogs:
        print(blog.owner, request.user.username)
        if blog.owner == user.username:
            blogs.append(blog)

    return render(request, "users/user.html", {"user": user, "blogs": blogs})
    

