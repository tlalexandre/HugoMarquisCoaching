# Generated by Django 3.2.23 on 2023-11-24 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendarapp', '0006_alter_course_actual_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='actual_participants',
        ),
        migrations.AddField(
            model_name='course',
            name='participants',
            field=models.ManyToManyField(related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_created', to=settings.AUTH_USER_MODEL),
        ),
    ]