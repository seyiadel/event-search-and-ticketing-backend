# Generated by Django 4.2.1 on 2023-07-05 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0002_remove_ticket_id_alter_ticket_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='uuid',
            new_name='id',
        ),
    ]
