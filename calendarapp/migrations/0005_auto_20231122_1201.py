# Generated by Django 3.2.23 on 2023-11-22 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0004_auto_20231122_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privatesession',
            old_name='description',
            new_name='type',
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.IntegerField(choices=[(0, 'Strength'), (1, 'Running'), (2, 'Stretch')], default=0),
        ),
        migrations.AddField(
            model_name='privatesession',
            name='location',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
