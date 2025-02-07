from django.urls import path, include

from .views import home, post_info, get_posts_by_category, create_post

app_name = 'blog'

urlpatterns = [
    path('home/', home, name='home'),
    path('post/<int:post_id>', post_info, name="post_info"),
    path("category/<int:category_id>", get_posts_by_category, name="get_posts_by_category"),
    path('create_post/', create_post, name="create_post")
]