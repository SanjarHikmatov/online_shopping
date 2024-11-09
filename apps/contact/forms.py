from django.forms import ModelForm

from apps.contact.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'