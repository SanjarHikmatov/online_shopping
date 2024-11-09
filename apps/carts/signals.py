from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.carts.models import ProductCard


@receiver((post_save, post_delete), sender=ProductCard)
def cart_saved(instance, **kwargs):
    instance.user.user_cart_count=ProductCard.objects.filter(user_id=instance.user.id).count()
    instance.user.save()




