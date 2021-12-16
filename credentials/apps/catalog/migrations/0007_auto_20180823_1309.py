# Generated by Django 1.11.15 on 2018-08-23 13:09


import sortedm2m.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("records", "0016_auto_20180822_1655"),
        ("catalog", "0006_auto_20180817_1929"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="creditpathway",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="creditpathway",
            name="programs",
        ),
        migrations.RemoveField(
            model_name="creditpathway",
            name="site",
        ),
        migrations.AlterField(
            model_name="pathway",
            name="programs",
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, related_name="pathways", to="catalog.Program"),
        ),
        migrations.DeleteModel(
            name="CreditPathway",
        ),
    ]
