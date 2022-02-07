from django.urls import path 
from .views import Blog_Home, Detail

urlpatterns = [
    path('', Blog_Home, name='blog-home'),
    path('<slug:slug>/', Detail, name='blog-home')
]