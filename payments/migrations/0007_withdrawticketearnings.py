# Generated by Django 4.2.1 on 2023-05-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0006_remove_bankdetail_receipient_code_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WithdrawTicketEarnings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
    ]