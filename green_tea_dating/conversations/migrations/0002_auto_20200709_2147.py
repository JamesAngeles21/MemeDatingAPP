# Generated by Django 3.0.8 on 2020-07-09 21:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversations',
            name='username1',
            field=models.ForeignKey(default='sender', on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversations',
            name='username2',
            field=models.ForeignKey(default='receiver', on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conversations',
            name='time_written',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 7, 9, 21, 47, 15, 102525)),
        ),
    ]