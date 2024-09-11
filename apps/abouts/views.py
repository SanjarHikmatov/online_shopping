from django.shortcuts import render

def about(request):
    return render(request, 'abouts_index.html')