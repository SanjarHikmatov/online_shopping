from django import forms

from apps.contact.models import Contact

class ContactForm(forms.ModelForm):

    # username = forms.CharField(
    #     required=False,
    #     max_length=200,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter the name'
    #         }
    #     )
    # )
    # email = forms.EmailField(
    #     required=False,
    #     widget=forms.EmailInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter email'
    #         }
    #     )
    # )
    # user_subject = forms.CharField(
    #     max_length=500,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter subject',
    #         }
    #     )
    # )
    #
    # user_message = forms.CharField(
    #     max_length=5000,
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Enter message',
    #         }
    #     )
    # )

    class Meta:
        model = Contact
        fields = '__all__'