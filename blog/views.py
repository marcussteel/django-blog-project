from multiprocessing import context
from tkinter import N
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.


def post_list(request):
    qs = Post.objects.all()
    context = {
        "object_list":qs
    }
    return render(request, "blog/post_list.html", context)

def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
    # form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            #şimdi user kimse o author olacak. form objesini kaydet ama database e gönderme diyoruz
            post = form.save(commit=False)
            print(request.user)
            post.author = request.user
            post.save()
            # urls'e  app_name = "blog"  ekleyerek hangi appteki list olduğunu belirlemiş olduk
            return redirect("blog:list")
    context = {
        'form':form
    }
    return render(request, "blog/post_create.html",context)