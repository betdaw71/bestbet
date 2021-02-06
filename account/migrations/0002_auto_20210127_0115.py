# Generated by Django 3.1.5 on 2021-01-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollar'), ('RUB', 'Ruble')], default='RUB', max_length=3),
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.IntegerField(default=7),
        ),
    ]
