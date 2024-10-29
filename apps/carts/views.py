from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from apps.carts.models import ProductCard


def cart_page(request):
    if request.user.is_authenticated:
        cart_user = ProductCard.objects.filter(user=request.user)
    else:
        cart_user = None
    context = {
        'cart_user': cart_user,
    }
    return render(request=request, template_name='cart.html', context=context)


@login_required
def create_cart(request, product_id):
    obj, create = ProductCard.objects.get_or_create(user_id=request.user.id, product_id=product_id)
    quantity = request.GET.get('cart_quantity', 1)

    if obj.quantity != quantity:
        obj.quantity = quantity
        obj.save()

    #
    # if not create:
    #     obj.delete()

    return redirect(request.META['HTTP_REFERER'])


def delete_cart(request, product_id):
    """
    This view deletes a Product Cart from the database.
    """
    if request.user.is_authenticated:
        ProductCard.objects.filter(user_id=request.user.id, product_id=product_id).delete()
    return redirect(request.META['HTTP_REFERER'])

