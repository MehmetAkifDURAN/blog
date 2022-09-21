from django.contrib import admin
from .models import BlogItem, BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'slug', 'blogger')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'blogger')
    list_filter = ('is_active', 'blogger')


class BlogItemAdmin(admin.ModelAdmin):
    list_display = ('content', 'item_type', 'order_number', 'blog_post')
    list_editable = ('order_number',)
    search_fields = ('content', 'blog_post')
    list_filter = ('item_type', 'blog_post')


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogItem, BlogItemAdmin)
