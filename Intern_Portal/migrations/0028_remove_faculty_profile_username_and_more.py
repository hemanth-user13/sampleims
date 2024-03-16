# Generated by Django 4.2.2 on 2023-09-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0027_myuploadedfiles_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty_profile',
            name='username',
        ),
        migrations.RemoveField(
            model_name='student_data',
            name='username',
        ),
        migrations.AddField(
            model_name='faculty_profile',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_data',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
