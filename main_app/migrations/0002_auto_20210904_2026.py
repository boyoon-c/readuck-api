# Generated by Django 3.2.6 on 2021-09-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='journalname',
            new_name='journal',
        ),
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
