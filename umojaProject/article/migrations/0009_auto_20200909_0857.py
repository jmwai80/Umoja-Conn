# Generated by Django 3.0.7 on 2020-09-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
