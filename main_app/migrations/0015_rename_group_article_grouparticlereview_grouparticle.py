# Generated by Django 3.2.6 on 2021-09-09 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_grouparticlereview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grouparticlereview',
            old_name='group_article',
            new_name='grouparticle',
        ),
    ]