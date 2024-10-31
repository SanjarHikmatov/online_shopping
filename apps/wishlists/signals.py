from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.wishlists.models import Wishlist


@receiver((post_save, post_delete), sender=Wishlist)
def wishlist_post_save(instance, **kwargs):
    instance.user.user_wishlist_count = Wishlist.objects.filter(user_id=instance.user_id).count()
    instance.user.save()
