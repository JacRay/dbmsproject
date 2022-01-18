from django.shortcuts import render
from .forms import DonorRegistration
from .models import DonorList
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import random


#Donnor forms display
def donorregdisplay(request):
    forms = DonorRegistration()
    if request.method == 'POST':
        forms = DonorRegistration(request.POST)
        if forms.is_valid():
            user = forms.save()
            email = user.email
            domain_name = get_current_site(request).domain
            token = str(random.random()).split('.')[1]
            user.token = token
            user.save()
            link = f'http://{domain_name}/donorreg/verify/{user.token}/{email}'
            send_mail(
            'Verify your email',
            f'Verify your email by clicking on the link {link}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
            msg = 'Please verify your email'
            context_details ={
                'forms' : forms,
                'msg' : msg
            }
            #After donor registation donor details display
            return render(request, 'registrations.html', context_details)
            return render(request,'info.html',{'msg':msg})
            print(forms.errors)
            context_details ={
                'forms' : forms
            }
            #After donor registation donor details display
            return render(request, 'registrations.html', context_details)

    context = {
                'forms' : forms,
            }

    return render(request, 'register.html', context)

def verify(request, tokenkey, emailid):
    try:
        user = DonorList.objects.get(token=tokenkey)
        if user.token == tokenkey:
            user.is_verified = True
            user.save()
            context_details ={
            'msg' : ' User Verified, Registration Succesfull',
            'user': user
            }
            return render(request, 'info.html', context_details)
        
    except Exception as e:
        msg = e
        return render(request, 'info.html', {'msg' : e})
