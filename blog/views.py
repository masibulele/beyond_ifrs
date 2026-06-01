from django.shortcuts import render 
from django.http import HttpResponse
from .models import Post, Catergory

# Create your views here.

def index(request):
    # retrieve all posts from database
    recent_posts = Post.objects.filter(section="recent")
    trending_posts = Post.objects.filter(section="trending")
    quick_posts = Post.objects.filter(section="quick_read")
    older_posts = Post.objects.filter(section="older_posts")
    cat_list = Catergory.objects.all()
    

    
    context= {"recent":recent_posts,
              "trending":trending_posts,
              "quick":quick_posts,
              "older": older_posts,
              "cats": cat_list
              }
    return render(request,"blog/index.html",context=context)

def post_details(request,post_id):
    return render(request, "blog/post.html")
