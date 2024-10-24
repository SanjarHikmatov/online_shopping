from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from apps.carts.models import ProductCard
from apps.products.models import Product


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

    product = get_object_or_404(Product, id=product_id)

    obj, create = ProductCard.objects.get_or_create(user_id=request.user.id, product_id=product.id)

    if not create:
        obj.delete()
    return redirect(request.META['HTTP_REFERER'])








def delete_cart(request, product_id):
    """
    This view deletes a Product Cart from the database.
    """
    if request.user.is_authenticated:
        ProductCard.objects.filter(user_id=request.user.id, product_id=product_id).delete()
    return redirect(request.META['HTTP_REFERER'])



#
# @login_required
# def increasing_cart(request, product_cart_id):
#     print(product_cart_id, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#     if request.method == 'POST':
#         product_cart = get_object_or_404(ProductCard, pk=product_cart_id)
#         if product_cart:
#             product_cart.quantity += int(request.POST.get('quantity'))
#             product_cart.save()
#     return redirect(request.META['HTTP_REFERER'])
