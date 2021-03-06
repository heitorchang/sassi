# Generated by Django 2.2.3 on 2020-05-25 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'ordering': ['name', 'address'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('upc', models.CharField(blank=True, max_length=32)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.ProductCategory')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('unit', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('notes', models.CharField(blank=True, max_length=200)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='markets.Brand')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.Market')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.Product')),
            ],
            options={
                'ordering': ['-purchase_date', 'product', 'brand', 'market'],
            },
        ),
    ]
