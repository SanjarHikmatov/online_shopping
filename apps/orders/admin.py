from django.contrib import admin

from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

    def has_add_permission(self, request):
        return False
