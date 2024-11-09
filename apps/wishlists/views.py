from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.products.models import Product
from apps.wishlists.forms import WishlistForm
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

@login_required
def wishlist_create(request):
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            product = get_object_or_404(Product, id=product_id)

            wish, created = Wishlist.objects.get_or_create(user=request.user, product=product)

            if not created:
                wish.delete()

            return redirect(request.META.get('HTTP_REFERER', 'products:product_list'))


def wishlist_delete(request, product_id):
    """
    This view deletes a wishlist from the database.
    """

    if request.user.is_authenticated:
        Wishlist.objects.filter(user_id=request.user.id, product_id=product_id).delete()
    return redirect(request.META['HTTP_REFERER'])












