# Generated by Django 2.2.7 on 2019-11-05 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=78)),
            ],
            options={
                'ordering': ['product', '-amount'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=78)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=78)),
                ('procedure', models.TextField(blank=True)),
                ('ingredients', models.ManyToManyField(to='fridge.Ingredient')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.Product'),
        ),
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('ingredients', models.ManyToManyField(to='fridge.Ingredient')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
