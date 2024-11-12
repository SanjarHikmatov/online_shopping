from django.contrib import messages
from django.shortcuts import redirect


from apps.coupons.models import Coupon, UsedCoupon


def check_coupon(request):

    code = request.POST.get('coupon_code')
    # if code is None:
    #     if request.session.get('coupon_data'):
    #         del request.session['coupon_data']
    #     messages.error(request, 'Coupon code is required')
    #     return redirect(request.META.get('HTTP_REFERER'))
    try:
        coupon = Coupon.objects.get(code=code)
    except Coupon.DoesNotExist:
        if request.session.get('coupon_data'):
            del request.session['coupon_data']
        messages.error(request, 'Coupon does not exist')
    else:
        if UsedCoupon.objects.filter(coupon_id=coupon.pk, user_id=request.user.pk).exists():
            if request.session.get('coupon_data'):
                del request.session['coupon_data']
            messages.warning(request, 'this coupon has alredy')
        else:
            request.session['coupon_data'] = {
                'pk': coupon.pk,
                'code': code,
                'discount_percent': coupon.discount_percent,
            }
            messages.success(request, 'is valid coupon')

    return redirect(request.META['HTTP_REFERER'])

