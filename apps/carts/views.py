from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.dateparse import parse_time
from pygments.lexer import default

from apps.carts.models import ProductCard
from django.db.models import F, Sum
from apps.coupons.models import UsedCoupon, Coupon

@login_required
def cart_page(request):
    user = request.user
    code = request.session.get('coupon_data', {}).get('code')
    if code is not None and UsedCoupon.objects.filter(coupon__code=code, user_id=user.pk).exists():
        del request.session['coupon_data']
    queryset = ProductCard.objects.annotate(total_price=F('quantity') * F('product__price')).filter(user=request.user)
    cart_total_price = queryset.aggregate(s=Sum('total_price',default=0))['s']
    context = {
        'cart_user': queryset.select_related('product'),
        'cart_total_price': cart_total_price,
    }
    return render(request=request, template_name='cart.html', context=context)


@login_required
def create_cart(request, product_id):
    obj, create = ProductCard.objects.get_or_create(user_id=request.user.id, product_id=product_id)
    quantity = request.POST.get('cart_quantity', 1)

    print(quantity)

    if obj.quantity != quantity:
        obj.quantity = quantity
        obj.save()

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




def set_cart_quantity(request, cart_id):
    if request.method != 'POST':
        return redirect('home-page')

    cart_obj = get_object_or_404(ProductCard, pk=cart_id)
    quantity = request.POST.get('item_quantity', cart_obj.quantity)
    if quantity.isdigit() and int(quantity) <= 0:
        cart_obj.delete()
    else:
        cart_obj.quantity = quantity
        cart_obj.save()
    return redirect(request.META['HTTP_REFERER'])