# Generated by Django 4.2.1 on 2023-05-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event_app", "0003_alter_eventinfo_end_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventinfo",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
    ]
