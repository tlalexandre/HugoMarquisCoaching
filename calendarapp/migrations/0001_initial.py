# Generated by Django 3.2.23 on 2023-11-21 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('private_slug', models.SlugField(unique=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('day_of_the_week', models.DateTimeField()),
                ('description', models.IntegerField(choices=[(0, 'Strength'), (1, 'Running'), (2, 'Stretch')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('course_slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('day_of_the_week', models.DateTimeField()),
                ('max_participants', models.IntegerField()),
                ('actual_participants', models.IntegerField()),
                ('location', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
