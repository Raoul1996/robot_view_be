# Generated by Django 2.0.6 on 2018-08-07 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RobotInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='neuq_robot', max_length=255, verbose_name='robot_name')),
                ('type', models.CharField(choices=[('car', 'car'), ('plane', 'plane')], default='car', max_length=100, verbose_name='robot_type')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'robot_info',
                'verbose_name_plural': 'robot_info',
            },
        ),
    ]
