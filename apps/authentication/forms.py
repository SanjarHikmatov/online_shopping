from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=20,
        min_length=4,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Username",
            }
        )
    )
    email = forms.EmailField(
        validators=[validate_password],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Email",
            }
        )
    )
    password = forms.CharField(
        validators=[validate_password],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Password",
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Confirm Password",
            }
        )
    )

    photo = forms.ImageField(required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("email already taken")
        return email

    def clean(self):
        data = super().clean()

        password = data['password']
        confirm_password = data['confirm_password']
        if password != confirm_password:
            raise ValidationError("Passwords do not match")
        return data



class UserLoginForm(forms.Form):
    email = forms.EmailField(
        validators=[validate_password],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Email",
            }
        )
    )
    password = forms.CharField(
        validators=[validate_password],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Password",
            }
        )
    )


