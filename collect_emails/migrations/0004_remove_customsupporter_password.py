# Generated by Django 4.1.3 on 2024-02-15 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect_emails', '0003_remove_customsupporter_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customsupporter',
            name='password',
        ),
    ]