from django.db import models

# Create your models here.
class EmployeeList(models.Model):
    name = models.CharField(max_length = 50, blank=True, null=True)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
    ]
    gender = models.CharField(
        max_length=6, blank=True, null=True,
        choices=gender_choices,
        )
    phone_number = models.IntegerField(blank=True, null=True)
    designation = models.CharField(max_length=10, blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
