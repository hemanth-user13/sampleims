# Generated by Django 4.2.2 on 2024-02-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0038_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
