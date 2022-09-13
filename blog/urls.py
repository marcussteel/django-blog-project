from django.urls import path, include
from .views import home, post_list

urlpatterns = [
    path('',post_list, name='list')
]