# Generated by Django 4.1.3 on 2024-02-15 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect_emails', '0002_remove_customsupporter_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customsupporter',
            name='last_login',
        ),
    ]