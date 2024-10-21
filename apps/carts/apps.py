from django.apps import AppConfig


class CardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.carts'

    def ready(self):
        import apps.carts.signals
