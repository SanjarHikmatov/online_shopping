from django.contrib import messages
from django.shortcuts import render, redirect

from apps.contact.forms import ContactForm
from apps.contact.models import Contact


def contact_us(request):

    contact_form = ContactForm(request.POST)
    context = {
        'contact_form': contact_form,
        'page': 'contact'
    }

    if request.method == 'POST':
        if contact_form.is_valid():
            contact_data = contact_form.cleaned_data

            contact, created = Contact.objects.get_or_create(
                 email=contact_data['email'],
                 defaults={
                     'first_name':contact_form.cleaned_data['first_name'],
                     'user_subject': contact_form.cleaned_data['user_subject'],
                     'user_message': contact_form.cleaned_data['user_message']
                 },

            )

            if created:
                messages.success = 'Success contact made so easy'
            else:
                messages.error = 'Somthing wrong'
            return render(request=request, template_name='contact.html', context={'messages': messages})
    else:
        contact_form = ContactForm(request.POST)

    return render(request=request, template_name='contact.html', context=context)

