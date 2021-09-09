# Generated by Django 3.2.6 on 2021-09-09 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0013_auto_20210907_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupArticleReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conntent', models.TextField(max_length=500)),
                ('group_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.grouparticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
