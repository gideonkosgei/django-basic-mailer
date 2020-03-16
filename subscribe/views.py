from django.shortcuts import render
from DjangoMailer.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to My application'
        message = 'Hope you are enjoying your stay.'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})