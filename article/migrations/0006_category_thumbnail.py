# Generated by Django 2.2 on 2019-04-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20190428_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='article/thumbnails/category/'),
        ),
    ]
