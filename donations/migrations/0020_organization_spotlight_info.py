# Generated by Django 3.1.1 on 2020-11-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0019_auto_20201123_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='spotlight_info',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
