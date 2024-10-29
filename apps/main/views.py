from django.shortcuts import render


def home(request):
    return render(request, template_name='index.html', context={'page': 'home'})





def checkout(request):
    return render(request, template_name='checkout.html', context={'page': 'pages'})





