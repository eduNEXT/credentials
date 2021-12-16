# Generated by Django 2.2.24 on 2021-08-17 19:06

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0023_auto_20210817_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredentialDateOverride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('date', models.DateField(help_text='The date to override a course certificate with. This is set in the LMS Django Admin.')),
                ('user_credential', models.OneToOneField(help_text='The id of the UserCredential that this date overrides', on_delete=django.db.models.deletion.CASCADE, related_name='date_override', to='credentials.UserCredential')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
