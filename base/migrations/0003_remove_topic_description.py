# Generated by Django 4.1.6 on 2023-02-08 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='Description',
        ),
    ]
