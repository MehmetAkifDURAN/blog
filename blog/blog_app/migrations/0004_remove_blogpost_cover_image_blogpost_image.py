# Generated by Django 4.0.1 on 2022-09-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_blogpost_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.FileField(null=True, upload_to='images', verbose_name='Kapak Resmi'),
        ),
    ]
