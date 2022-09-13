from email import contentmanager
from email.mime import image
from multiprocessing import AuthenticationError
from tabnanny import verbose
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT )
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title



    # title
    # content
    # image
    # category
    # publishdate
    # lastupdated
    # Author 
    # status draft published
    # slug field  örn django how-to-learn-django