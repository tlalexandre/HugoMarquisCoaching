# Generated by Django 3.2.23 on 2023-11-20 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0004_auto_20231120_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='privatesession',
            name='coach',
        ),
        migrations.DeleteModel(
            name='Coach',
        ),
    ]