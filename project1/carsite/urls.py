from django.urls import path, include

from .views import items_list

app_name = 'carsite'

urlpatterns = [
    path('carsite/', items_list, name='carsite'),
]