# Generated by Django 2.2.7 on 2019-11-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0007_auto_20191105_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
