# Generated by Django 4.0 on 2022-01-19 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreg', '0005_remove_donorlist_is_verified_remove_donorlist_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donorlist',
            old_name='last_donate_date',
            new_name='date',
        ),
    ]