# Generated by Django 3.1.3 on 2020-11-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskManagerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='contract_id_unique',
            field=models.CharField(blank=True, help_text='Номер не должен повторяться', max_length=500, null=True, unique=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='verification',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Отметка'),
        ),
    ]
