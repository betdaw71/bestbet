# Generated by Django 3.1.5 on 2021-01-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210127_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='default-user.jpeg', upload_to='account'),
        ),
    ]