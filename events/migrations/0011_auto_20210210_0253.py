# Generated by Django 3.1.5 on 2021-02-10 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20210210_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='active',
        ),
        migrations.AddField(
            model_name='match',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]