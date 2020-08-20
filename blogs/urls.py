from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^blog/(?P<blog_id>[0-9]+)/$", views.blog, name="blog"), 
    url(r"^new/", views.new_blog, name="new-blog"), 
    url(r"^edit/(?P<blog_id>[0-9]+)/$", views.edit_blog, name="edit-blog"), 
    url(r"^delete/(?P<blog_id>[0-9]+)/$", views.delete_blog, name="delete-blog"), 
]
