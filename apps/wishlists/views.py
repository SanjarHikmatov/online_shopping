from django.contrib import messages
from django.shortcuts import render, redirect

from apps.wishlists.models import Wishlist

def wishlist_page(request):
    context = {
        'wishlists': Wishlist.objects.select_related('user', 'product'),
    }
    return render(request=request, template_name="wishlist.html", context=context)


def wishlist_create(request, product_id):
    """
    This view is used to create a new Wishlist
    """
    if request.user.is_authenticated:
            Wishlist.objects.get_or_create(user_id=request.user.id, product_id=product_id)
    else:
        messages.error(request, "You must be logged in to create a new wishlist.")
    return redirect('products:product_list')

def wishlist_delete(request, product_id):
    """
    This view deletes a wishlist from the database.
    """
    if request.user.is_authenticated:
        Wishlist.objects.filter(user_id=request.user.id, product_id=product_id).delete()

    return redirect('wishlists:wishlist-page')
