# Generated by Django 4.2.2 on 2023-09-23 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0025_myuploadedfiles_roll_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuploadedfiles',
            name='student',
        ),
    ]