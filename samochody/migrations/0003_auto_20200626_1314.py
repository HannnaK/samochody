# Generated by Django 3.0.5 on 2020-06-26 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samochody', '0002_auto_20200623_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='fuels',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='makes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='models',
            options={'managed': False},
        ),
    ]
