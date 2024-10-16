from django.contrib import messages
from django.shortcuts import render, redirect

from apps.products.models import Product
from apps.wishlists.models import Wishlist


def wishlist_page(request):
    if request.user.is_authenticated:
        wishlists_user = Wishlist.objects.filter(user=request.user).select_related('product')
    else:
        wishlists_user = None
    context = {
        # 'wishlists': Wishlist.objects.select_related('user', 'product'),
        'wishlists': wishlists_user,
    }
    return render(request=request, template_name="wishlist.html", context=context)


def wishlist_create(request, product_id):
    """
    This view is used to create a new Wishlist
    """
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        obj, creat = Wishlist.objects.get_or_create(user_id=request.user.id, product=product)

        if not creat:
            obj.delete()
    # else:
    #     messages.error(request, "You must be logged in to create a new wishlist.")

    return redirect(request.META['HTTP_REFERER'])


def wishlist_delete(request, product_id):
    """
    This view deletes a wishlist from the database.
    """

    if request.user.is_authenticated:
        Wishlist.objects.filter(user_id=request.user.id, product_id=product_id).delete()
    return redirect(request.META['HTTP_REFERER'])












