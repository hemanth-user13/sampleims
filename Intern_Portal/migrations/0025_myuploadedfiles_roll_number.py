# Generated by Django 4.2.2 on 2023-09-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0024_delete_uploadedfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuploadedfiles',
            name='roll_number',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]