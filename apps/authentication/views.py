
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib import messages

from config.settings import LOGIN_REDIRECT_URL

from apps.authentication.forms import UserRegisterForm
from apps.authentication.models import CustomUser


def login_page(request):
    return render(request=request, template_name='auth/auth-login-basic.html')


def user_login(request):
    email = request.POST['email']
    password = request.POST.get('password')
    try:
        user = CustomUser.objects.get(email=email)
        if user.check_password(password):
            login(request, user)
            return redirect('home-page')

    except CustomUser.DoesNotExist:
        pass

    messages.error(request, 'Invalid username or password.')
    return redirect('login-page')


def user_logout(request):
    logout(request)
    return redirect(LOGIN_REDIRECT_URL)


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
    form_obj = UserRegisterForm(data=request.POST)

    if form_obj.is_valid():
        form_obj.cleaned_data.pop('confirm_password')
        messages.success(request, 'Register success')
        get_user_model().objects.get_or_create(
            email=form_obj.cleaned_data['email'],
            defaults={
                'username': form_obj.cleaned_data['username'],
                'password': make_password(form_obj.cleaned_data['password']),
            }
        )

    messages.error(request, form_obj.errors)
    return redirect(settings.LOGIN_URL)