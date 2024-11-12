from django.contrib import messages
from django.db import transaction
from apps.carts.models import ProductCard
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.general.models import General, PaymentMethod
from apps.orders.forms import OrdersForm


def checkout(request):
    carts = ProductCard.objects.filter(user=request.user).select_related('product')
    if not carts:
        return redirect('carts:cart-page')

    try:
        shipping_percent = General.objects.first().shipping_percent
    except AttributeError:
        shipping_percent = 0
    coupon_discount_percent = request.session.get('coupon_data', {}).get('discount_percent', 0)
    total_cart = sum([cart.quantity * cart.product.price for cart in carts])

    # ===== total sum =============

    total_sum = total_cart + total_cart * shipping_percent // 100 - total_cart * coupon_discount_percent // 100

    payment_methods = PaymentMethod.objects.order_by('name')
    context = {
        'carts': carts,
        'page': 'pages',
        'shipping_percent': shipping_percent,
        'total_cart': total_cart,
        'total_sum': total_sum,
        'payment_methods': payment_methods,
    }
    return render(request=request, template_name='checkout.html', context=context)



@login_required
@transaction.atomic
def create_order(request):
    if request.method == 'GET':
        return redirect('home-page')

    form = OrdersForm(data=request.POST)
    print(request.POST)
    if form.is_valid():
        order = form.save(commit=False)
        order.user = request.user
        order.save()
        messages.success(request, 'Your order has been created!')
    else:
        messages.error(request, form.errors)
    if request.session.get('coupon_data'):
        del request.session['coupon_data']
    return redirect(request.META.get('HTTP_REFERER'))