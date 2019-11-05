# Generated by Django 2.2.7 on 2019-11-05 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0005_remove_recipe_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=78)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.Product')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.Recipe')),
            ],
            options={
                'ordering': ['recipe', 'product', 'amount'],
            },
        ),
    ]
