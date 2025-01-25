# Generated by Django 4.2.17 on 2025-01-25 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_tournamentuser_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentroom',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournamentroom',
            name='started',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tournamentroom',
            name='tournament_size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournamentuser',
            name='state',
            field=models.CharField(default='WAITING', max_length=255),
            preserve_default=False,
        ),
    ]
