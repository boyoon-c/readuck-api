# Generated by Django 3.2.6 on 2021-09-05 00:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0006_auto_20210905_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]