# Generated by Django 3.0.7 on 2020-09-05 06:39

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20200905_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fellowship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True, verbose_name='Posted')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AddField(
            model_name='internship',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internship',
            name='internship_company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 9, 5, 6, 39, 37, 331892, tzinfo=utc), verbose_name='Posted Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='program',
            name='program_company',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
