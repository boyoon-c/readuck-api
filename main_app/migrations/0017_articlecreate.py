# Generated by Django 3.2.6 on 2021-09-09 08:01

from django.db import migrations, models
import django.views.generic.edit


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_rename_conntent_grouparticlereview_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(django.views.generic.edit.CreateView, models.Model),
        ),
    ]
