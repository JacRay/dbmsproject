# Generated by Django 4.0 on 2022-01-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipientlist',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]