# Generated by Django 2.1.1 on 2019-04-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190411_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='sections',
        ),
        migrations.RemoveField(
            model_name='section',
            name='is_main',
        ),
        migrations.AddField(
            model_name='section',
            name='articles',
            field=models.ManyToManyField(related_name='sections', to='articles.Article'),
        ),
    ]
