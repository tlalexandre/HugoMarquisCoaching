# Generated by Django 3.2.23 on 2023-12-11 11:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0013_alter_privatesession_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatesession',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]