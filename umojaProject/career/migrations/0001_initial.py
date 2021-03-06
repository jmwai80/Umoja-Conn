# Generated by Django 3.0.7 on 2020-09-11 10:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
