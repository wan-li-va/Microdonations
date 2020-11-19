# Generated by Django 3.1.1 on 2020-11-19 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donations', '0012_auto_20201118_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='covfefe',
        ),
        migrations.AddField(
            model_name='task',
            name='task_owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
