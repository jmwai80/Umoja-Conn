# Generated by Django 3.0.7 on 2020-09-29 18:58

from django.db import migrations
import django.utils.timezone
import trix.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20200928_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='content2',
            field=trix.fields.TrixField(default=django.utils.timezone.now, verbose_name='Content'),
            preserve_default=False,
        ),
    ]
