from random import choices
from django import forms
from django.forms import ModelForm
from .models import RecipientList
from employee.models import EmployeeList

class RecipientRegistration(forms.ModelForm):
    class Meta:
        model = RecipientList
        fields = ('name', 
        'gender',
        'date_of_birth',
        'blood_group',
        'staff',
        'phone_number',
        'email',
        'occupation',
        'home_address',
        'date')
        staff : forms.ModelChoiceField(queryset=EmployeeList.objects.all(), empty_label="Select Staff", widget=forms.Select(attrs={'class':'form-control'}))
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'blood_group' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'phone_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control', 'required':'True'}),
            'home_address' : forms.Textarea(attrs={'class':'form-control', 'required':'True'}),
            'date' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
        }
        