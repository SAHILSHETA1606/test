# Generated by Django 4.0.1 on 2022-06-23 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='medicine_power',
            new_name='medicine_type',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='medicine_price',
        ),
    ]
