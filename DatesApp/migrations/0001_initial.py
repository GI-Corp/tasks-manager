# Generated by Django 3.1.3 on 2020-11-26 12:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TasksDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True, verbose_name='Рабочий день')),
            ],
            options={
                'verbose_name_plural': 'Даты',
            },
        ),
    ]
