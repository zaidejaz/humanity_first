# Generated by Django 4.1.3 on 2024-02-15 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collect_emails', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customsupporter',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customsupporter',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customsupporter',
            name='is_staff',
        ),
    ]