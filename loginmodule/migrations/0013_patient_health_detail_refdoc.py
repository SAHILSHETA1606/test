# Generated by Django 4.0.1 on 2022-06-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginmodule', '0012_patient_detail_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_health_detail',
            name='refdoc',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
