from django.urls import path, include

from .views import home, post_info

app_name = 'blog'

urlpatterns = [
    path('home/', home, name='home'),
    path('post/<int:post_id>', post_info, name="post")
]