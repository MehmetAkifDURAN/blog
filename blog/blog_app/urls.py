from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('blog-post/<slug:slug>', views.blogPost, name='blog_post')
]
