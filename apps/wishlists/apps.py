from django.apps import AppConfig


class WishlistsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.wishlists'


    def ready(self):
        import apps.wishlists.signals
