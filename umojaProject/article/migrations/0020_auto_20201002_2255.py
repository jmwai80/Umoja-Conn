# Generated by Django 3.0.7 on 2020-10-02 22:55

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_auto_20201002_2249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fellowship',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AlterModelOptions(
            name='internship',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AlterModelOptions(
            name='program',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AddField(
            model_name='gallery',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Posted'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 10, 2, 22, 55, 34, 430664, tzinfo=utc), verbose_name='Posted'),
            preserve_default=False,
        ),
    ]
