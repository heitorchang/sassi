# Generated by Django 3.0.8 on 2020-07-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0010_diaryentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=78, unique=True),
        ),
    ]
