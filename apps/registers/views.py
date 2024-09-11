from django.shortcuts import render, redirect
from django.contrib import messages

from apps.users.models import CosUser


def register(request):
    return render(request, 'reg_index.html')


def user_register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not all([username, email, password]):
        messages.error(request, 'All fields are required.')
        return redirect('register-page')

    else:
        user = CosUser.objects.create_user(username=username, email=email, password=password)

    return redirect('login-page')