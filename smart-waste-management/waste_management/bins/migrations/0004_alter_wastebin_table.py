# Generated by Django 4.2.20 on 2025-05-10 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bins", "0003_wastebin_created_at"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="wastebin",
            table="bins_waste_bin",
        ),
    ]
