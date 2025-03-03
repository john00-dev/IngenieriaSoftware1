# Generated by Django 5.1 on 2025-03-03 06:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_is_on_vacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='contact_number',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
