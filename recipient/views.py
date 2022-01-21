from django.shortcuts import render
from .forms import RecipientRegistration
from .models import RecipientList
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import random

# Create your views here.

def recipient_registration(request):
    forms = RecipientRegistration()
    if request.method == 'POST':
        forms = RecipientRegistration(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, 'recipregistrations.html', {'forms':forms})
    else:
        forms = RecipientRegistration()
    return render(request, 'recipreg.html', {'forms':forms})