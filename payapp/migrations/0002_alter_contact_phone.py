# Generated by Django 4.2 on 2023-04-07 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact", name="phone", field=models.IntegerField(),
        ),
    ]
