# from lib2to3.fixes.fix_input import context
#
# from django.contrib import messages
#
# from django.conf import settings
# from django.shortcuts import render, redirect
#
# from apps.card.forms import ProductCardForm
# from apps.card.models import ProductCard
#
#
# def card_page(request):
#     if request.user.is_authenticated:
#         card_user = ProductCard.objects.filter(user=request.user)
#     else:
#         card_user = None
#
#     context = {
#         'card_user': card_user,
#     }
#     return render(request=request, template_name='cart.html', context=context)
#
# def create_card_list(request, product_id):
#     if request.method == 'GET':
#         return redirect(settings.LOGIN_REDIRECT_URL)
#     product = ProductCard.objects.get(pk=product_id)
#     card_form = ProductCardForm(data=request.POST)
#     if card_form.is_valid():
#         messages.success(request, 'your card has been saved')
#         user = card_form.cleaned_data['user']
#
#         card, created = ProductCard.objects.get_or_create(user_id=request.user.id, product=product)
#         if created:
#             card.delete()
#
#
#
#     else:
#         messages.error(request, card_form.errors)
#
#     return redirect(request.META.get('HTTP_REFERER'))
