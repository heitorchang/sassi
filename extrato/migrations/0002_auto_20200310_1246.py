# Generated by Django 2.2.7 on 2020-03-10 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extrato', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'ordering': ['-data', '-id'], 'verbose_name_plural': 'Transações'},
        ),
    ]
