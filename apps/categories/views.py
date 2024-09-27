
from django.shortcuts import render

from apps.categories.models import Category


def category(request):
    categories = Category.objects.select_related('category').all()
    context = {'categories': categories}
    return render(request, 'index.html', context)



