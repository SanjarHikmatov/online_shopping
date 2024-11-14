from django.http import HttpResponse
from django.db.models import Q, Count

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from apps.carts.models import ProductCard
from apps.comments.models import ProductComment
from apps.products.models import Product
from apps.wishlists.models import Wishlist
from apps.features.models import Feature, FeatureValue


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = ProductComment.objects.filter(product_id=product.pk).order_by('-created_at').select_related('product')
    comments_page = request.GET.get('comment_page', 1)

    try:
        user_cart_quantity = ProductCard.objects.get(product_id=pk, user=request.user).quantity
    except ProductCard.DoesNotExist:
        user_cart_quantity = 1
    context = {
        'user_cart_quantity': user_cart_quantity,
        'comments': comments,
        'comments_page_obj': Paginator(comments, 2).get_page(comments_page),
        'product': product
    }
    return render(request, template_name='detail.html', context=context)


def product_by_feature(request, pk):
    return redirect('products:detail-page', pk)


def product_list(request: WSGIRequest) -> HttpResponse:
    user = request.user
    cart_user = []
    user_wishlist = []

    if user.is_authenticated:
        cart_user = ProductCard.objects.filter(user_id=user.pk).values_list('product_id', flat=True)
        user_wishlist = Wishlist.objects.filter(user_id=user.pk).values_list('product_id', flat=True)

    search_text = request.session.get('search_text', None)
    cat_id = request.session.get("cat_id", None)
    queryset = Product.objects.order_by('-pk')
    best_rating = request.session.get('best-rating', None)
    avg_rating = request.GET.get('avg_rating')
    features = []

    if cat_id:
        features = Feature.objects.filter(category_id=cat_id).prefetch_related('values')
        # =============== bu qisimda biz sorovlar oshganu uchun
        #  har bir feature valuelarni aylanganda ularga
        #  ulangan productlar sonini aylanib olib keldik
        #  sorovlarni kamaytirish uchun ===========================
        feature_values = FeatureValue.objects.filter(
            feature__category_id=cat_id
        ).annotate(products_count=Count(
            'product_features_values'
        )
        ).select_related('feature')

        features = {}

        for feature_value in feature_values:
            item = {
                'pk': str(feature_value.pk),
                'name': feature_value.name,
                'products_count': feature_value.products_count,

            }

            if feature_value.feature.pk not in features:
                features[feature_value.feature.pk] = {
                    'pk': str(feature_value.feature.pk),
                    'name': feature_value.feature.name,
                    'values': [item]
                }

            else:
                features[feature_value.feature.pk]['values'].append(item)

        features = list(features.values())
        print(features)
        queryset = queryset.filter(
            Q(category_id=cat_id)
            |
            Q(category__parent_id=cat_id)

        )

    elif avg_rating:
        queryset = queryset.filter(avg_rating__gte=avg_rating)

    elif best_rating:
        queryset = queryset.order_by(
            '-avg_rating'
        )

    elif search_text:
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

    # ================ filer by feature_values ===========
    feature_values = request.GET.getlist('feature_values', [])
    # feature_values = list(map(int, feature_values))
    request.session['feature_values'] = str(feature_values)

    if feature_values:
        queryset = queryset.filter(product_features__feature_values__id__in=feature_values).distinct()


    page_number = request.GET.get("page1", 1)
    paginator_obj = Paginator(queryset, 9)
    page_obj = paginator_obj.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'user_wishlist': user_wishlist,
        'cart_user': cart_user,
        'features': features,
    }

    return render(request=request, template_name='shop.html', context=context)


def product_sort_by_avg_rating(request):
    if 'best-rating' in request.session:
        del request.session['best-rating']
    else:
        request.session['best-rating'] = 'best-rating'

    return redirect(request.META['HTTP_REFERER'])
