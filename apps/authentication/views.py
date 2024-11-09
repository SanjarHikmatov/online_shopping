
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, get_user_model

from apps.authentication.forms import UserRegisterForm


def login_page(request):
    return render(request=request, template_name='auth/auth-login-basic.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect(request.META.get('HTTP_REFERER'))

def user_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = get_user_model().objects.get(email=email)
        if user.check_password(password):
            login(request, user)
            return redirect('home-page')
    except ObjectDoesNotExist:
        messages.error(request, 'xatolik.')
    messages.error(request, 'Invalid email or password.')
    return redirect(settings.LOGIN_URL)

def register_page(request):
    context = {
        'forms': UserRegisterForm,
    }
    return render(request=request, template_name='auth/auth-register-basic.html', context=context)


def user_register(request):
    if request.method == 'GET':
        context = {
            'forms': UserRegisterForm,
        }
        return render(request, 'auth/auth-register-basic.html', context)
    form_obj = UserRegisterForm(data=request.POST, )
    try:

        if form_obj.is_valid() and form_obj.cleaned_data['confirm_password'] == form_obj.cleaned_data['password']:
            form_data = form_obj.cleaned_data.copy()
            form_data.pop('confirm_password')

            messages.success(request, 'Register success')
            get_user_model().objects.get_or_create(
                email=form_obj.cleaned_data['email'],
                defaults={
                    'photo': form_obj.cleaned_data['photo'],
                    'first_name': form_obj.cleaned_data['first_name'],
                    'password': make_password(form_obj.cleaned_data['password']),
                }
            )
            return redirect(settings.LOGIN_URL)

        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('authentications:register-page')

    except KeyError:
        pass
    messages.error(request, form_obj.errors)
    return redirect(request.META.get('HTTP_REFERER'))