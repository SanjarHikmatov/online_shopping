from django.contrib import messages


from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login


def home(request):

    return render(request, template_name='index.html')

def shop(request):
    return render(request, template_name='shop.html')

def detail(request):
    return render(request, template_name='detail.html')

def contact(request):
    return render(request, template_name='contact.html')

def checkout(request):
    return render(request, template_name='checkout.html')

def cart(request):
    return render(request, template_name='cart.html')

def about(request):
    return render(request, template_name='about.html')

def login_page(request):
    return render(request, template_name='login.html')

def user_login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(email=email, password=password)
    if user is not None:
        messages.error(request, 'Invalid username or password')
        return redirect('login-page')
    login(request, user)
    return render(request, template_name='index.html')