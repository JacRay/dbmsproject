from django.db import models
from employee.models import EmployeeList
# Create your models here.

class RecipientList(models.Model):
    name = models.CharField(max_length = 50, blank=True, null=True)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
    ]
    gender = models.CharField(
        max_length=6, blank=True, null=True,
        choices=gender_choices,
        )
    date_of_birth = models.DateField(blank=True, null=True)
    blood_choices=[
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),

    ]
    blood_group = models.CharField(
        max_length=4, blank=True, null=True,
        choices=blood_choices
        )
    staff = models.ForeignKey(EmployeeList, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    occupation = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.name