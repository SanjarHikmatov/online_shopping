from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from apps.comments.models import ProductComment
from apps.features.models import Feature
from apps.product_features.models import ProductFeature
from apps.products.models import Product
from apps.wishlists.models import Wishlist
from django.db.models import Q


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = ProductComment.objects.filter(product_id=product.pk).order_by('-created_at')

    comments_page = request.GET.get('comment_page', 1)


    context = {
        'comments': comments,
        'product': product,
        'comments_page_obj': Paginator(comments, 2).get_page(comments_page),
    }
    return render(request, template_name='detail.html', context=context)

def product_by_feature(request, pk):
    return redirect('products:detail-page', pk)

def product_list(request: WSGIRequest) -> HttpResponse:
    user = request.user
    user_cart = []
    user_wishlist = []

    if user.is_authenticated:
        user_cart = Wishlist.objects.filter(user_id=user.pk).values_list('product_id', flat=True)
        user_wishlist = Wishlist.objects.filter(user_id=user.pk).values_list('product_id', flat=True)

    search_text = request.session.get('search_text', None)
    cat_id = request.session.get("cat_id", None)
    queryset = Product.objects.order_by('-pk')

    if cat_id:
        queryset = queryset.filter(
            Q(category_id=cat_id)
            |
            Q(category__parent_id=cat_id)
        )

    if search_text:
        queryset = queryset.filter(
            Q(title_uz__icontains=search_text)
            |
            Q(title_ru__icontains=search_text)
            |
            Q(title_en__icontains=search_text)
            |
            Q(short_description_uz__icontains=search_text)
            |
            Q(short_description_ru__icontains=search_text)
            |
            Q(short_description_en__icontains=search_text)
        )

    page_number = request.GET.get("page1", 1)
    if isinstance(page_number, int):
        page_number = int(page_number)
    else:
        page_number = 1

    paginator_obj = Paginator(queryset, 9)
    page_obj = paginator_obj.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'user_wishlist': user_wishlist,
        'user_cart': user_cart,
    }

    return render(request=request, template_name='shop.html', context=context)
