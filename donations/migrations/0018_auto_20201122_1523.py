# Generated by Django 3.1.1 on 2020-11-22 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0017_auto_20201121_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='is_spotlighted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='organization',
            name='organization_img_link',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
