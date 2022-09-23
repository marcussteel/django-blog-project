from importlib import import_module
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # biz django.contrib.auth import views as auth_views i komple aldık, bunun içinden istediğimizi alacağız
    # name : login olmak zorunda gereklilik
    path('/login', auth_views.LoginView.as_view , name='login'),

]
