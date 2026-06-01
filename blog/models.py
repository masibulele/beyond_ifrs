from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.

class Catergory(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True, null=True, default=None)
    image = models.ImageField(upload_to="images",blank=True)

    class Meta:
        verbose_name_plural = "Catergories"

    def __str__(self):
        return self.name
    
   

class Post(models.Model):
    STATUS = {
        ("0", "Draft"),
        ("1", "Publish")


    }

    SECTION ={
        ("recent","Recent"),
        ("trending","Trending"),
        ("older_posts", "Older Posts"),
        ("quick_read","Quick Read")

    }

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images")
    author = models.CharField(max_length=100, default="admin")
    cat = models.ForeignKey(Catergory,on_delete=models.CASCADE, related_name="categories")
    published_at = models.DateTimeField(auto_now_add=True)
    post_slug = AutoSlugField(populate_from="title",  unique=True, null=True, default=None)
    status = models.CharField(choices=STATUS,max_length=1,default=0)
    section = models.CharField(choices=SECTION,max_length=100,default="recent")

    def __str__(self):
        return self.title
