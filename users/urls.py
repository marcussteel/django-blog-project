
import imp
from importlib import import_module
from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register,profile

app_name = "users"

urlpatterns = [
    # biz django.contrib.auth import views as auth_views i komple aldık, bunun içinden istediğimizi alacağız
    # name : login olmak zorunda gereklilik
    path('login', auth_views.LoginView.as_view (template_name="users/login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name="users/logout.html"), name='logout'),
    path('register/', register, name='register' ),
    path('profile/', profile, name='profile'),

]
