# Generated by Django 3.0.8 on 2020-07-09 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_auto_20200709_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversations',
            name='time_written',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 7, 9, 21, 48, 55, 494403)),
        ),
    ]
