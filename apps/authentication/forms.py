# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.password_validation import validate_password
# from django.core.exceptions import ValidationError
#
# from .validations import validate_username
#
#
# class UserRegisterForm(forms.Form):
#     username = forms.CharField(max_length=50,
#                                required=True,
#                                validators=[validate_username],
#                                widget=forms.TextInput(
#                                    attrs={
#                                        'class': 'form-control',
#                                        'placeholder': 'Enter your username',
#                                    }))
#     email = forms.EmailField(
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         )
#     )
#     password = forms.CharField(
#         min_length=8,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         ),
#         validators=[
#             validate_password,
#         ]
#     )
#
#     re_password = forms.CharField(
#         min_length=8,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         ),
#         validators=[
#             validate_password,
#         ]
#     )
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if get_user_model().objects.filter(username=username).exists():
#             raise ValidationError("Username already exists")
#
#         return username
#
#     def clean(self):
#         data = super().clean()
#         re_password = data['re_password']
#         password = data['password']
#         if re_password != password:
#             raise ValidationError("Passwords do not match")
#
#         return data
