from apps.categories.models import Category

def categories_contex(request, *args, **kwargs):
    context = {
        'categories': Category.objects.filter(parent__isnull=True).prefetch_related('children'),
    }
    return context