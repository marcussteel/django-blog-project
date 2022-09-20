from multiprocessing import context
from tkinter import N
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm
from .models import Post
from django.template.defaultfilters import slugify
# Create your views here.


def post_list(request):
    qs = Post.objects.filter(status="p")
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


def post_detail(request, slug):
    form = CommentForm()


    print("request.user : ", request.user)
    print("request : ", request)
    # print("request.get : ", request.get)

    obj = get_object_or_404(Post, slug = slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            print("request.user : ",request.user)
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = obj
            comment.save()
            return redirect("blog:detail", slug=slug)
    context = {
    'object':obj,
    'form' :form
    }
    return render(request, "blog/post_detail.html",context)

def post_update(request,slug):
    #Post.objects.get(slug=lerafsdf-dgdfg-fghfg-h )
    obj = get_object_or_404(Post, slug=slug) # bu slugtakileri bul bana  listele demek
    #if req pos ise yerine bunu kullandık
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("blog:list")
    context={
        "object":obj,
        "form":form
    }
    return render(request, "blog/post_update.html", context)

def post_delete(request,slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("blog:list")
    context = {
        "object": obj,
        }
    return render(request, "blog/post_delete.html", context)
