# Generated by Django 3.0.7 on 2020-09-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20200927_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='admin_approved',
        ),
        migrations.RemoveField(
            model_name='article',
            name='name',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=500, verbose_name='Writer'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Title'),
        ),
    ]
