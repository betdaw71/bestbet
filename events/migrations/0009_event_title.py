# Generated by Django 3.1.5 on 2021-02-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_sport_sport_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
