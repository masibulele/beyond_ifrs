from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Catergory(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True, null=True, default=None)

    class Meta:
        verbose_name_plural = "Catergories"

    def __str__(self):
        return self.name
    
   

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images")
    author = models.CharField(max_length=100, default="admin")
    cat = models.ForeignKey(Catergory,on_delete=models.CASCADE, related_name="categories")
    published_at = models.DateTimeField(auto_now_add=True)
    post_slug = AutoSlugField(populate_from="title",  unique=True, null=True, default=None)

    def __str__(self):
        return self.title
