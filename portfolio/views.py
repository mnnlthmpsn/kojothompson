from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Portfolio
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'index.html', {'portfolios': portfolios})

def mail_me(request):
    if request.method == 'POST':
        subject = 'YOUR PORTFOLIO SITE'
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message'] + ' from ' +name + ' : ' + email
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mnnlthmpsn@outlook.com',]

        send_mail( subject, message, email_from, recipient_list )
        messages.add_message(request, messages.SUCCESS, 'Mail Sent')
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))