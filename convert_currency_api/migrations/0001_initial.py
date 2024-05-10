# Generated by Django 4.2 on 2023-04-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Rate",
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
                ("currency1", models.CharField(default="gbp", max_length=200)),
                ("currency2", models.CharField(default="gbp", max_length=200)),
                (
                    "rate",
                    models.DecimalField(decimal_places=2, default=1, max_digits=10),
                ),
            ],
        ),
    ]
