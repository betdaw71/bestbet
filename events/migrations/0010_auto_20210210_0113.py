# Generated by Django 3.1.5 on 2021-02-10 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event',
            name='win',
            field=models.BooleanField(default=False),
        ),
    ]
