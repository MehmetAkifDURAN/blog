from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(verbose_name='Başlık', unique=True, max_length=50)
    description = models.TextField(verbose_name='Açıklama', max_length=500)
    image = models.FileField(
        upload_to='images', verbose_name='Kapak Resmi', null=True)
    is_active = models.BooleanField(verbose_name='Aktif Mi', default=False)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True)
    blogger = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name='Yazar', related_name='blog_posts')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'

    def __str__(self):
        return f'{self.title} - {self.blogger}'


class BlogItem(models.Model):
    ITEM_TYPE_CHOICES = [
        ('Text', 'Metin'),
        ('Code', 'Kod'),
    ]
    content = models.TextField(verbose_name='İçerik')
    item_type = models.CharField(
        verbose_name='İçerik Tipi', max_length=5, choices=ITEM_TYPE_CHOICES)
    order_number = models.IntegerField('Sıra Numarası')
    blog_post = models.ForeignKey(
        to=BlogPost, on_delete=models.CASCADE, verbose_name="Blog Yazısı", related_name='items')

    class Meta:
        verbose_name = 'Blog Öğesi'
        verbose_name_plural = 'Blog Öğeleri'

    def __str__(self):
        return f'{self.content[:20]} - {self.blog_post}'