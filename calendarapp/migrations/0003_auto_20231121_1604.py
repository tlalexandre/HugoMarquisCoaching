# Generated by Django 3.2.23 on 2023-11-21 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0002_auto_20231121_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='privatesession',
            old_name='private_slug',
            new_name='slug',
        ),
    ]
