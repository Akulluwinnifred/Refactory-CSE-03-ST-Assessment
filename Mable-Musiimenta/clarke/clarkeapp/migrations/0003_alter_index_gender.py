# Generated by Django 5.0.6 on 2024-05-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clarkeapp", "0002_alter_index_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="index",
            name="gender",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female")],
                default="Male",
                max_length=50,
            ),
        ),
    ]
