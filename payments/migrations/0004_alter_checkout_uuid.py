# Generated by Django 4.2.1 on 2023-07-03 02:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_checkout_uuid_alter_checkout_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=34),
        ),
    ]
