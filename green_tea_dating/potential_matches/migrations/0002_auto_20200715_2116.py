# Generated by Django 3.0.8 on 2020-07-15 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('potential_matches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PotentialMatches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swipedOn', models.BooleanField(default=False)),
                ('potential_matched', models.ForeignKey(default='potential_matched', on_delete=django.db.models.deletion.CASCADE, related_name='potential_matched', to=settings.AUTH_USER_MODEL)),
                ('potential_matcher', models.ForeignKey(default='potential_matcher', on_delete=django.db.models.deletion.CASCADE, related_name='potential_matcher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('potential_matcher', 'potential_matched')},
            },
        ),
        migrations.DeleteModel(
            name='Potential_Matches',
        ),
    ]
