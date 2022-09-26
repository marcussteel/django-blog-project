from http.client import HTTPResponse
from multiprocessing import context
from tkinter import N
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, PostForm
from .models import Like, Post
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def post_list(request):
    qs = Post.objects.filter(status="p")
    context = {
        "object_list":qs
    }
    return render(request, "blog/post_list.html", context)

@login_required()
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
            messages.SUCCESS(request, "Post created succesfully")
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


@login_required()
def post_update(request,slug):
    #Post.objects.get(slug=lerafsdf-dgdfg-fghfg-h )
    obj = get_object_or_404(Post, slug=slug) # bu slugtakileri bul bana  listele demek
    #if req pos ise yerine bunu kullandık
    if request.user.id != obj.author.id:
        messages.WARNING(request, "You r nor a author of this tag")
        return redirect("blog:list", slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.SUCCESS(request, "Post updated succesfully")
        return redirect("blog:list")
    context={
        "object":obj,
        "form":form
    }
    return render(request, "blog/post_update.html", context)


@login_required()
def post_delete(request,slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.user.id != obj.author.id:
        return HTTPResponse('You are not authorized !')
    if request.method == "POST":
        obj.delete()
        messages.SUCCESS(request, "Post deleted succesfully")
        return redirect("blog:list")
    context = {
        "object": obj,
        }
    return render(request, "blog/post_delete.html", context)


@login_required()
def like(request, slug):
    if request.method == "POST":
        obj = obj = get_object_or_404(Post, slug=slug)
        # artık hangi posta like yapacağımı biliyorum
        like_qs = Like.objects.filter(user=request.user, post=obj)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect("blog:detail", slug=slug)
    return redirect("blog:detail", slug=slug)

