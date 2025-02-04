from django.urls import path, include

from .views import items_list

app_name = 'blog'

urlpatterns = [
    path('items/', items_list, name='items'),
]