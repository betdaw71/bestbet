# Generated by Django 3.1.6 on 2021-02-12 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20210212_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='express',
            name='win',
            field=models.BooleanField(default=False),
        ),
    ]
