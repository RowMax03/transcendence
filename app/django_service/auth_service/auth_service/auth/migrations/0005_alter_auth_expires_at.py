# Generated by Django 3.2.16 on 2024-12-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0004_auto_20241230_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='expires_at',
            field=models.DateField(),
        ),
    ]
