from django.shortcuts import render


def home(request):
    return render(request, template_name='index.html', context={'page': 'home'})


def shop(request):
    return render(request, template_name='shop.html', context={'page': 'shop'})


def detail(request):
    return render(request, template_name='detail.html', context={'page': 'pages'})


def contact(request):
    return render(request, template_name='contact.html', context={'page': 'contact'})


def checkout(request):
    return render(request, template_name='checkout.html', context={'page': 'pages'})


def cart(request):
    return render(request, template_name='cart.html', context={'page': 'pages'})


def about(request):
    return render(request, template_name='about.html', context={'page': 'about'})


def wishlist(request):
    return render(request, template_name='wishlist.html', context={'page': 'wishlist'})
