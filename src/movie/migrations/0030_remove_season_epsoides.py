# Generated by Django 4.1.2 on 2022-10-22 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0029_remove_series_seasons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='season',
            name='epsoides',
        ),
    ]
