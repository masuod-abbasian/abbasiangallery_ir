from django.urls import path 
from .views import Blog_Home, Detail, category

app_name = 'Blog'
urlpatterns = [
    path('', Blog_Home, name='blog-home'),
    path('page/<int:page>', Blog_Home, name='blog-home'),
    path('article/<slug:slug>/', Detail, name='detail'),
    path('category/<slug:slug>/', category , name='category'),
]