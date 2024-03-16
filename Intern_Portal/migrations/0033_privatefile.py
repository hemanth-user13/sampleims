# Generated by Django 4.2.2 on 2024-01-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0032_remove_hod_profile_username_hod_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='private_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]