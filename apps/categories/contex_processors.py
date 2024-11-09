# from apps.categories.models import Category
#
# def categories_contex(request, *args, **kwargs):
#     context = {
#         'categories': Category.objects.prefetch_related('children', 'products').filter(parent__isnull=True),
#     }
#     return context
