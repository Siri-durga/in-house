# Generated by Django 5.0.3 on 2024-04-19 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0027_addexamhall_rooms_list_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Rooms',
            },
        ),
    ]
