# Generated by Django 5.0.6 on 2024-06-06 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guestapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weather', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('google_map_link', models.URLField()),
                ('image', models.ImageField(upload_to='destinations/')),
                ('description', models.TextField()),
                ('by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guestapp.usertable')),
            ],
        ),
    ]