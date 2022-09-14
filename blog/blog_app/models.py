from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(verbose_name='Başlık', unique=True, max_length=50)
    description = models.TextField(verbose_name='Açıklama', max_length=500)
    cover_image = models.FileField(
        verbose_name='Kapak Resmi', upload_to='images')
    is_active = models.BooleanField(verbose_name='Aktif Mi', default=False)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True)
    blogger = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name='Yazar', related_name='blog_posts')


class Code(models.Model):
    code = models.TextField(verbose_name='Kod')
    order_number = models.IntegerField(verbose_name='Sıra No')
    blog_post = models.ForeignKey(
        to=BlogPost, on_delete=models.CASCADE, verbose_name='Blog Yazısı', related_name='codes')


class Text(models.Model):
    text = models.TextField(verbose_name='Metin')
    order_number = models.IntegerField(verbose_name='Sıra No')
    blog_post = models.ForeignKey(
        to=BlogPost, on_delete=models.CASCADE, verbose_name='Blog Yazısı', related_name='texts')
