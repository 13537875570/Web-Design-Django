# Generated by Django 3.1.2 on 2020-11-01 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_newstory_sum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newstory',
            old_name='score',
            new_name='num',
        ),
        migrations.AddField(
            model_name='newstory',
            name='ave',
            field=models.FloatField(default=0),
        ),
    ]
