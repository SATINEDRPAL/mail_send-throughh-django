from django.shortcuts import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def mail(request):
    subject ='Be Positive'
    msg = "Always Be Positive"
    to ="palstindrsingh@gmail.com"
    res = send_mail(subject,msg,settings.EMAIL_HOST_USER,[to] )
    if(res ==1):
        msg ="Mail Sent Sucessfully"
    else:
        msg ="Mail Could Not Sent"
    return HttpResponse(msg)