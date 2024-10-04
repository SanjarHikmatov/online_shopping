from django.apps import AppConfig


class ProductRatingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ratings'

def ready(self):
    from apps.ratings import signals