from django.contrib import messages
from django.shortcuts import redirect

from apps.coupons.models import Coupon, UsedCoupon


def check_coupon(request):

    code = request.POST.get('code')

    if code is None:
        return redirect('home-page')
    try:
        coupon = Coupon.objects.get(code=code)

    except Coupon.DoestNotExist:
        messages.error(request, 'not valid coupon')
    else:
        if UsedCoupon.objects.filter(coupon_id=coupon.pk, user_id=request.user.pk).exists():
            messages.warning(request, 'this coupon has alredy')
        else:
            request.session['coupon_data'] = {
                'code': code,
                'discount_percent': coupon.discount_percent
            }
            messages.success(request, 'is valid coupon')

    return redirect(request.META['HTTP_REFERER'])