# Generated by Django 5.0.3 on 2024-05-17 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techApp', '0002_rename_entry_scheme_student_entry_scheme_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='date_Of_Birth',
            new_name='date_of_birth',
        ),
    ]
