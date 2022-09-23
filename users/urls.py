import imp
from importlib import import_module
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register



urlpatterns = [
    # biz django.contrib.auth import views as auth_views i komple aldık, bunun içinden istediğimizi alacağız
    # name : login olmak zorunda gereklilik
    path('login', auth_views.LoginView.as_view , name='login'),
    path('logout', auth_views.LogoutView.as_view , name='logout'),
    path('register/', register , name='register'),

]
