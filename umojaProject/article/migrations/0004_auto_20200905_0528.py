# Generated by Django 3.0.7 on 2020-09-05 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='img', verbose_name='Add Photos to Article'),
        ),
    ]