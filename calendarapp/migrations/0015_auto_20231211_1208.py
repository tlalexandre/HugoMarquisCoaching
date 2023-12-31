# Generated by Django 3.2.23 on 2023-12-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0014_privatesession_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='day_of_week',
            field=models.IntegerField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='is_recurrent',
            field=models.BooleanField(default=False),
        ),
    ]
