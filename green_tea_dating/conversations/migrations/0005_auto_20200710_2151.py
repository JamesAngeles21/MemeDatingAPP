# Generated by Django 3.0.8 on 2020-07-10 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0004_auto_20200709_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversations',
            old_name='conversation_id',
            new_name='id',
        ),
    ]
