from django.db import models
from employee.models import EmployeeList

#Donor resistration forms data table
class DonorList(models.Model):
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
    # is_verified = models.BooleanField(default=False, blank=True)
    # token = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    any_diseases_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    any_diseases = models.CharField(
        max_length=4, blank=True, null=True,
        choices=any_diseases_choices,
        default="no"
        )
    allergies_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    allergies = models.CharField(
        max_length=4, blank=True, null=True,
        choices=allergies_choices,
        default="no"
        )
    cardiac_choices=[
        ("yes","Yes"),
        ("no", "No"),
    ]
    cardiac = models.CharField(
        max_length=4, blank=True, null=True,
        choices=cardiac_choices,
        default="no"
        )
    bleeding_disorders_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    bleeding_disorders = models.CharField(
        max_length=4, blank=True, null=True,
        choices=bleeding_disorders_choices,
        default="no"
        )
    hbsAg_hcv_hIV_choices=[
        ("yes","Yes"),
        ("no","No"),
    ]
    hbsAg_hcv_hIV =models.CharField(
        max_length=4, blank=True, null=True,
        choices=hbsAg_hcv_hIV_choices,
        default="no"
        )



    def __str__(self):
        return self.name



