# Generated by Django 3.0.7 on 2020-09-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20200926_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fellowship',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='program',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]
