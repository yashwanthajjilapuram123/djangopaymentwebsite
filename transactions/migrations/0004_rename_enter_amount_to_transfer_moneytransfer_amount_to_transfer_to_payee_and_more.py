# Generated by Django 4.2 on 2023-04-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_moneytransfer_payee_currency_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="moneytransfer",
            old_name="enter_amount_to_transfer",
            new_name="amount_to_transfer_to_payee",
        ),
        migrations.RenameField(
            model_name="moneytransfer",
            old_name="enter_payee_email_address",
            new_name="payee_email_address",
        ),
        migrations.RenameField(
            model_name="moneytransfer",
            old_name="enter_your_email_address",
            new_name="payer_email_address",
        ),
        migrations.AlterField(
            model_name="amount",
            name="email",
            field=models.EmailField(default="your_email", max_length=100),
        ),
    ]
