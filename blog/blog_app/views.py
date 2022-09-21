from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.


def index(request):
    blog_posts = BlogPost.objects.filter(is_active=True)
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog_app/index.html', context)


def blogPost(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    blog_post_items = blog_post.items.all().order_by('order_number')
    context = {
        'blog_post': blog_post,
        'blog_post_items': blog_post_items
    }
    return render(request, 'blog_app/blog-post.html', context)
