from django.shortcuts import render

from apps.contact.forms import ContactForm
from apps.contact.models import Contact


def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_data = contact_form.cleaned_data

            contact, created = Contact.objects.get_or_create(
                user_subject=contact_data['user_subject'],
                user_message=contact_data['user_message'],

            )
            if created:
                print('nima gap')
                message = 'Success contact made so easy'
            else:
                message = 'Somthing wrong'
            return render(request=request, template_name='contact.html', context={'message': message})

    else:
        contact_form = ContactForm()
    return render(request=request, template_name='contact.html', context={'contact_form': contact_form, 'page': 'contact'})
