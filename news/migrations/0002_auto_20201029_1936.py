# Generated by Django 3.1.2 on 2020-10-29 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newstory',
            old_name='score',
            new_name='year',
        ),
    ]
