from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
        url(r"^login/$", login, {"template_name": "users/login.html"}, name="login"),
        url(r"^logout/$", views.logout_view, name="logout"), 
        url(r"^register/$", views.register, name="register"),
        url(r"^list/$", views.list_user, name="list"), 
        url(r"^user/(?P<user_id>[a-z A-Z]+)/$", views.user, name="user"), 
]
