from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from apps.ratings.models import ProductRating


@receiver([post_save, post_delete], sender=ProductRating)
def product_rating_post_save_and_delete(instance: ProductRating, **kwargs):
    # ===== set related product avg rating =======
    instance.product.set_avg_rating()
