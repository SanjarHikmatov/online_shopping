from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from apps.users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    readonly_fields = (
        "last_login",
        "date_joined",
        "user_cart_count",
        "user_wishlist_count",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields":
                    (
                        "first_name",
                        "last_name",
                        "user_cart_count",
                        "user_wishlist_count",
                        "photo"
                    )
            }
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)
