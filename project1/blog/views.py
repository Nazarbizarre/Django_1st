from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post


def home(request):
  categories = Category.objects.all()
  posts = Post.objects.all()
  data = {"categories":categories, "posts":posts}
  return render(request, "index.html", context=data)


def post_info(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  return render(request, "post_info.html", {'post':post})
  
def get_posts_by_category(request, category_id):
  categories = Category.objects.all()
  category = get_object_or_404(Category, id=category_id)
  posts = Post.objects.filter(category=category)
  data = {"categories":categories, "posts":posts}
  return render(request, 'index.html', context=data)
  
def create_post(request):
  categories = Category.objects.all()
  if request.method == 'POST':
    title = request.POST.get('title')
    body = request.POST.get('body')
    category_id = request.POST.get('category')
    category = get_object_or_404(Category, id=int(category_id))
    try:
      post = Post(title=title, body=body, category=category)
      post.full_clean()    
    except:
      return HttpResponse('<h1>Bad Values</h1>')
    else:
      post.save()
      
    return redirect('blog:home')
  return render(request, "create_post.html", context={"categories":categories})