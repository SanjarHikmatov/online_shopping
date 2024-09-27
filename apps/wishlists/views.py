from django.shortcuts import render

def wishlist_view(request):
    return render(request=request, template_name="wishlist.html")