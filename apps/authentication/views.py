from django.conf import settings
# from django.contrib.auth.models import User, AbstractUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, login_not_required

from config.settings import LOGIN_REDIRECT_URL, LOGIN_URL


# from apps.authentication.forms import UserRegisterForm
from .models import CustomUser


def login_page(request):
    return render(request=request, template_name='auth/auth-login-basic.html')


def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = CustomUser.objects.get(username=username)
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
    return render(request=request, template_name='auth/auth-register-basic.html')


def user_register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not all([username, email, password]):
        messages.error(request, 'All fields are required.')
        return redirect('register-page')
    user, created = get_user_model().objects.get_or_create(username=username)
    if created:
        user.email = email
        user.set_password(password)
        user.save()
    else:
        messages.error(request, 'Username or password already taken.')
        return redirect('register-page')
    messages.success(request, 'Registration successful.')
    return redirect(LOGIN_URL)
