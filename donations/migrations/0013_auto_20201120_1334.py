# Generated by Django 3.1.1 on 2020-11-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0012_organization_organization_img_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='organization_img_link',
            field=models.CharField(default='https://i.imgur.com/ARKtpJh.png', max_length=200),
        ),
    ]
