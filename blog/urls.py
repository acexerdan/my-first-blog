from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

# ignore domain name, match empty string, tells Django to go to views.post_list 
# if someone enters the website at the 'http://127.0.0.1:8000/' address.
# post_list is the name of the URL used to identify the view

# <int:pk>: Django expects an integer value and will transfer it to a view as a variable called pk.