# Generated by Django 4.0.1 on 2022-09-21 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_remove_blogpost_cover_image_blogpost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('item_type', models.CharField(choices=[('Text', 'Metin'), ('Code', 'Kod')], max_length=5, verbose_name='İçerik Tipi')),
                ('order_number', models.IntegerField(verbose_name='Sıra Numarası')),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='blog_app.blogpost', verbose_name='Blog Yazısı')),
            ],
            options={
                'verbose_name': 'Blog Öğesi',
                'verbose_name_plural': 'Blog Öğeleri',
            },
        ),
        migrations.RemoveField(
            model_name='text',
            name='blog_post',
        ),
        migrations.DeleteModel(
            name='Code',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
    ]
