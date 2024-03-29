# Generated by Django 3.0.8 on 2020-07-13 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20200710_2309'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('swipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='swipe',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='swipe',
            unique_together={('user', 'content')},
        ),
        migrations.RemoveField(
            model_name='swipe',
            name='profile',
        ),
    ]
