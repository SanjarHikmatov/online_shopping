from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from apps.products.models import Product


def product_list(request: WSGIRequest) -> HttpResponse:
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)
    paginator_obj = Paginator(Product.objects.order_by('-pk'), 9)
    page_obj = paginator_obj.get_page(page_number)
    print(paginator_obj.__dict__)
    print(page_obj.__dict__)

    context = {
        'page_obj': page_obj,
    }
    return render(request=request, template_name='shop.html', context=context)