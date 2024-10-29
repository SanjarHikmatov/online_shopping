from django import forms



class ContactForm(forms.Form):

    user_subject = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter subject',
            }
        )
    )

    user_message = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter message',
            }
        )
    )

    