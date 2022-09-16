from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def index(request):
    blog_posts = BlogPost.objects.filter(is_active=True)
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog_app/index.html', context)
