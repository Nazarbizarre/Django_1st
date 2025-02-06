from django.shortcuts import render, get_object_or_404
from .models import Category, Post


def home(request):
  categories = Category.objects.all()
  posts = Post.objects.all()
  data = {"categories":categories, "posts":posts}
  return render(request, "index.html", context=data)


def post_info(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  return render(request, "post.html", {'post':post})
  
  
 