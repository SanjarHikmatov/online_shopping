from django.contrib import admin

from apps.general.models import General, PaymentMethod


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    pass

    def has_add_permission(self, request):
        return not General.objects.exists()


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass
