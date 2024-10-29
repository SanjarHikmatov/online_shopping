from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from apps.carts.models import ProductCard
from apps.comments.models import ProductComment
from apps.products.models import Product
from apps.wishlists.models import Wishlist
from django.db.models import Q, Avg


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = ProductComment.objects.filter(product_id=product.pk).order_by('-created_at')
    comments_page = request.GET.get('comment_page', 1)

    try:
        user_cart_quantity = ProductCard.objects.get(product_id=pk, user=request.user).quantity
    except ProductCard.DoesNotExist:
        user_cart_quantity = 1
    context = {
        'user_cart_quantity': user_cart_quantity,
        'comments': comments,
        'product': product,
        'comments_page_obj': Paginator(comments, 2).get_page(comments_page),
        'product': product
    }
    return render(request, template_name='detail.html', context=context)

def product_by_feature(request, pk):
    return redirect('products:detail-page', pk)

def product_list(request: WSGIRequest) -> HttpResponse:
    user = request.user
    user_cart = []
    user_wishlist = []

    if user.is_authenticated:

        user_cart = ProductCard.objects.filter(user_id=user.pk).values_list('product_id', flat=True)
        user_wishlist = Wishlist.objects.filter(user_id=user.pk).values_list('product_id', flat=True)

    search_text = request.session.get('search_text', None)
    cat_id = request.session.get("cat_id", None)
    queryset = Product.objects.order_by('-pk')
    avg_sort_rating = request.session.get('avg-sort-rating')
    if cat_id:
        print(cat_id,'{{{{{{{{{{{{{{{{{{{{{{{')
        queryset = queryset.filter(
            Q(category_id=cat_id)
            |
            Q(category__parent_id=cat_id)
        )
    if avg_sort_rating:
        print(avg_sort_rating,"_________________________))))))))")
        queryset = queryset.filter(
            category__product__avg_rating=avg_sort_rating
        )
    if search_text:
        print(search_text,"====================")
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
    paginator_obj = Paginator(queryset, 9)
    page_obj = paginator_obj.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'user_wishlist': user_wishlist,
        'user_cart': user_cart,
    }

    return render(request=request, template_name='shop.html', context=context)



def product_sort_by_avg_rating(request, product_id):
    # product = Product.objects.filter(product_id=product_id.avg_rating)
    avg_sort_rating = request.POST.get(product_id.avg_rating, None)
    request.session['avg_sort_rating'] = avg_sort_rating
    print(request.session['avg_sort_rating'],'PPPPPPPPPPPPPPPPPPPPPPPPP')
    return redirect('products:product_list')
