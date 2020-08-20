from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import models


def index(request):
    blogs = models.Blog.objects.all()
    return render(request, "index.html", {"blogs": blogs})

def blog(request, blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    return render(request, "blog.html", {"blog": blog})


@login_required
def new_blog(request):
    if request.method == "GET":
        return render(request, "new-blog.html")

    elif request.method == "POST":
        blog_title = request.POST["title"]
        blog_text = request.POST["text"]
        blog_owner = request.user
        blog = models.Blog()
        blog.title = blog_title
        blog.text = blog_text
        blog.owner = blog_owner.username
        blog.save()
        return HttpResponseRedirect("/")


@login_required
def edit_blog(request, blog_id):
    if request.method == "GET":
        blog = models.Blog.objects.get(id=blog_id)
        return render(request, "edit-blog.html", {"blog": blog})

    elif request.method == "POST":
        blog_text = request.POST["text"]
        blog = models.Blog.objects.get(id=blog_id)
        if blog.owner != request.user.username and request.user.username != "rain":
            return render(request, "error.html", {"errormsg": "怎么，想编辑别人的文章? 你觉得我会让吗? "})
        blog.text = blog_text
        blog.save()
    return HttpResponseRedirect("/")


@login_required
def delete_blog(request, blog_id):
    # if this-blog.owner != user-now-login and user-now-login != administrator-user (rain)
    blog = models.Blog.objects.get(id=blog_id)
    if blog.owner != request.user.username and request.user.username != "admin":
        return render(request, "error.html", {"errormsg": "怎么了，想删除别人的文章? 没门! "})
    
    blog.delete()
    return HttpResponseRedirect("/")

        


def error404(request):
    return HttpResponseRedirect("404.html")

def error500(request):
    return HttpResponseRedirect("500.html")
