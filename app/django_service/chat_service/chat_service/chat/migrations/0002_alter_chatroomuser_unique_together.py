# Generated by Django 4.2.17 on 2025-02-01 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chatroomuser',
            unique_together={('user_id', 'chat_room')},
        ),
    ]
