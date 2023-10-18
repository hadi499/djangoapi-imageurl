from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.getPosts, name='posts'),
    path('posts/create/', views.createPost, name='create')
]
