# Generated by Django 2.2.17 on 2021-01-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_page_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
