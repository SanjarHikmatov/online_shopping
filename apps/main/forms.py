# from django import forms
# from django.contrib.auth import get_user_model
# from django.core.exceptions import ValidationError
# from django.contrib.auth.password_validation import validate_password
#
#
# class UserRegisterForm(forms.Form):
#     username = forms.CharField(
#         max_length=20,
#         min_length=4,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 "placeholder": "Username",
#             }
#         )
#     )
#     email = forms.EmailField(
#         validators=[validate_password],
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 "placeholder": "Email",
#             }
#         )
#     )
#     password = forms.CharField(
#         validators=[validate_password],
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 "placeholder": "Password",
#             }
#         )
#     )
#
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#                 "placeholder": "Confirm Password",
#             }
#         )
#     )
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if get_user_model().objects.filter(username=username).exists():
#             raise ValidationError("Username already taken")
#         return username
#
#     def clean(self):
#         data = super().clean()
#
#         password = data['password']
#         confirm_password = data['confirm_password']
#         if password != confirm_password:
#             raise ValidationError("Passwords do not match")
#         return data
