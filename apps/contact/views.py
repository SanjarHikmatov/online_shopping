from django.contrib import messages
from django.shortcuts import render, redirect

from apps.contact.forms import ContactForm
from apps.contact.models import Contact


def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Success contact made so easy')
            return render(request=request, template_name='contact.html')
        else:
            messages.error(request, contact_form.errors)
    return render(request=request, template_name='contact.html')

