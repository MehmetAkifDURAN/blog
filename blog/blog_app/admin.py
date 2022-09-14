from django.contrib import admin
from .models import BlogPost, Code, Text
# Register your models here.

# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'is_active', 'unit_price', 'slug',
#                     'instructor', 'category_level_two')
#     prepopulated_fields = {'slug': ('name',)}
#     search_fields = ('name', 'description')
#     list_filter = ('is_active', 'instructor', 'category_level_two')
# admin.site.register(Course, CourseAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'slug', 'blogger')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'blogger')
    list_filter = ('is_active', 'blogger')


class CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'order_number', 'blog_post')
    search_fields = ('blog_post',)
    list_filter = ('blog_post',)


class TextAdmin(admin.ModelAdmin):
    list_display = ('text', 'order_number', 'blog_post')
    search_fields = ('text', 'blog_post')
    list_filter = ('blog_post',)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Code, CodeAdmin)
admin.site.register(Text, TextAdmin)
