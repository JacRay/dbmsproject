from django.urls import path
from .views import donorregdisplay,verify
#, donorregsuccess

urlpatterns = [
    path('', donorregdisplay, name='dregsite'),
    path('donors', donorregdisplay, name='dregdisplay'),
    path('verify/<str:tokenkey>/<str:emailid>', verify, name='dregverify')
]