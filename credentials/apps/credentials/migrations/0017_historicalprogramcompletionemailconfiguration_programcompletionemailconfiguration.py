# Generated by Django 2.2.17 on 2020-11-18 22:57

import django.db.models.deletion
import django_extensions.db.fields
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("credentials", "0016_credential_content_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProgramCompletionEmailConfiguration",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified"),
                ),
                (
                    "identifier",
                    models.CharField(
                        help_text='Should be either "default" to affect all programs, the program type slug, or the UUID of the program. Values are unique.',
                        max_length=50,
                        unique=True,
                    ),
                ),
                (
                    "html_template",
                    models.TextField(
                        help_text="For HTML emails.Allows tags include (a, b, blockquote, div, em, i, li, ol, span, strong, ul)"
                    ),
                ),
                (
                    "plaintext_template",
                    models.TextField(help_text="For plaintext emails. No formatting tags. Text will send as is."),
                ),
                ("enabled", models.BooleanField(default=False)),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HistoricalProgramCompletionEmailConfiguration",
            fields=[
                ("id", models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name="ID")),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified"),
                ),
                (
                    "identifier",
                    models.CharField(
                        db_index=True,
                        help_text='Should be either "default" to affect all programs, the program type slug, or the UUID of the program. Values are unique.',
                        max_length=50,
                    ),
                ),
                (
                    "html_template",
                    models.TextField(
                        help_text="For HTML emails.Allows tags include (a, b, blockquote, div, em, i, li, ol, span, strong, ul)"
                    ),
                ),
                (
                    "plaintext_template",
                    models.TextField(help_text="For plaintext emails. No formatting tags. Text will send as is."),
                ),
                ("enabled", models.BooleanField(default=False)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")], max_length=1),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical program completion email configuration",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
