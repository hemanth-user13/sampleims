# Generated by Django 4.2.2 on 2024-02-15 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0042_circular'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='application_url',
            field=models.URLField(default=2),
            preserve_default=False,
        ),
    ]