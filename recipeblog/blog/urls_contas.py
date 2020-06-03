from django.conf.urls import url
from django.contrib	import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('/login/', auth_views.LoginView.as_view(template_name="/blog/login.html"), name="login"),
	path('/logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]