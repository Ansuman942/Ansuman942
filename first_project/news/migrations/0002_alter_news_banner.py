# Generated by Django 5.1 on 2024-09-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='banner',
            field=models.ImageField(upload_to='news_banners/'),
        ),
    ]
