# Generated by Django 4.2.1 on 2023-06-27 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0006_alter_eventinfo_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
