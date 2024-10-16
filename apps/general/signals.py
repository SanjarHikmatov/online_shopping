import os
from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save
from django.db.models import ImageField, FileField


@receiver(post_delete)
def delete_related_images(instance, **kwargs):
    for field in instance.__class__._meta.get_fields():
        if isinstance(field, (ImageField, FileField)):
            file = getattr(instance, field.name)
            if file and os.path.exists(file.path):
                os.remove(file.path)



@receiver(pre_save)
def update_related_images(sender, instance, **kwargs):
    if not instance.pk:
        return

    for field in sender._meta.get_fields():
        if isinstance(field, (ImageField, FileField)):
            old_file = getattr(sender.objects.get(pk=instance.pk), field.name)
            new_file = getattr(instance, field.name)

            if old_file and old_file != new_file and os.path.exists(old_file.path):
                os.remove(old_file.path)
                