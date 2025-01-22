from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView

from apps.carts.models import ProductCard
from django.db.models import F, Sum
from apps.coupons.models import UsedCoupon
from apps.general.models import General


class CartPageListView(LoginRequiredMixin, ListView):
    """  """
    allow_empty = False
    template_name = 'cart.html'
    context_object_name = 'object_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            shipping_percent = General.objects.first().shipping_percent
        except AttributeError:
            shipping_percent = 0


        cart_total_price = 0
        queryset  = self.get_queryset()

        if queryset:
            cart_total_price = queryset.aggregate(
                s=Sum('total_price', default=0)
            )['s'] or 0

        context['shipping_percent'] = shipping_percent
        context['cart_total_price'] = cart_total_price

        return context

    def get_queryset(self):
        user = self.request.user
        code = self.request.session.get('coupon_data', {}).get('code')

        if code is not None and UsedCoupon.objects.filter(
                coupon__code=code,
                user_id=user.pk).exists():
            del self.request.session['coupon_data']

        queryset = ProductCard.objects.annotate(
            total_price=F('quantity') * F('product__price')
        ).filter(user=self.request.user)
        return queryset



class CreateCartView(LoginRequiredMixin, CreateView):
    fields = '__all__'
    model = ProductCard
    template_name = 'cart.html'
    success_url = '/HTTP_REFERER/'

    def form_valid(self, form):
        obj, create = self.model.objects.get_or_create(
            user_id=self.request.user.pk,
            product_id=form.cleaned_data['product_id'],
        )
        quantity = self.request.POST.get('cart_quantity', 1)

        if obj.quantity != quantity:
            obj.quantity = quantity
            obj.save()

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