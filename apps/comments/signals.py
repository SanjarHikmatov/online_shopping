from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from apps.comments.models import ProductComment
from django.db.models import Avg

@receiver((post_delete, post_save), sender=ProductComment)
def comment_post_save_or_post_delete(instance, *args, **kwargs):
    instance.product.comment_count = ProductComment.objects.filter(product_id=instance.product.id).count()
    instance.product.avg_rating = ProductComment.objects.filter(product_id=instance.product.id).aggregate(Avg('rating'))['rating__avg']
    instance.product.save()