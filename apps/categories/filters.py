from django.contrib.admin import SimpleListFilter

class CategoryFilter(SimpleListFilter):
    title = 'Category degree'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return [
            ('main_cat', 'Main category'),
            ('low_cat', 'Lower category'),
        ]

    def queryset(self, request, queryset):
        match self.value():
            case 'main_cat':
                return queryset.filter(parent__isnull=True)
            case 'low_cat':
                return queryset.filter(parent__isnull=False, category__isnull=True)
        return queryset
