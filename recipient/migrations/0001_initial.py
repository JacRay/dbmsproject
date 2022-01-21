# Generated by Django 4.0 on 2022-01-19 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipientList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=6, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('o+', 'O+'), ('o-', 'O-'), ('ab+', 'AB+'), ('ab-', 'AB-')], max_length=4, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('occupation', models.CharField(blank=True, max_length=10, null=True)),
                ('home_address', models.TextField(blank=True, null=True)),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employeelist')),
            ],
        ),
    ]
