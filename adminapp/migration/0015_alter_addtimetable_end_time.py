# Generated by Django 5.0.3 on 2024-03-30 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_alter_addtimetable_batch_alter_addtimetable_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtimetable',
            name='end_time',
            field=models.TimeField(default='15:30'),
        ),
    ]
