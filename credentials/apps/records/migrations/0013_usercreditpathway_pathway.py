# Generated by Django 1.11.15 on 2018-08-20 20:32


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_auto_20180817_1929"),
        ("records", "0012_auto_20180801_2000"),
    ]

    operations = [
        migrations.AddField(
            model_name="usercreditpathway",
            name="pathway",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="catalog.Pathway"),
        ),
    ]
