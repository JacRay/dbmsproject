from django.urls import path
from .views import recipient_registration

urlpatterns = [
    path('', recipient_registration, name='rregsite'),
    path('donors', recipient_registration, name='rregdisplay'),
]