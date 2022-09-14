from distutils.command.upload import upload
from email import contentmanager
from email.mime import image
from email.policy import default
from importlib.resources import contents
from multiprocessing import AuthenticationError
from tabnanny import verbose
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#media yüklendiğinde media nın içinde blog oluşturaacak 0 yerine id si ile , 1 yeride ise dosya ismi ile bir klasöt oluşturup içine atacak
def user_directory_path(instance, filename):
    return 'blog/{0}/{1}.format(instance.author.id, filename)'


class Category(models.Model):
    name = models.CharField(max_length=100)
# Burası admin panelde Categorys görünmesi yerine Categories olarak  görünmesi için
    class Meta:
        verbose_name_plural = 'Categories'
# Burası admin panelde veya ilk çağırılan yerde default hangi başlığın görüeceğini tespit eder
    def __str__(self):
        return self.name



class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='smileicon.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT )
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time_stamp =  models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
