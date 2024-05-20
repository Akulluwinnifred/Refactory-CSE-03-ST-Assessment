# Generated by Django 5.0.6 on 2024-05-17 10:44

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreg',
            name='f_name',
            field=models.CharField(max_length=50, validators=[core.models.validate_letters]),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='l_name',
            field=models.CharField(max_length=50, validators=[core.models.validate_letters]),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='residence',
            field=models.CharField(max_length=255, validators=[core.models.validate_letters]),
        ),
    ]
