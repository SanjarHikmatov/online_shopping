from django.db.models.signals import pre_save
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver

from apps.abouts.models import About


@receiver(pre_save, sender=About)
def about_pre_save(instance, **kwargs):
    instance.title = ' '.join(instance.title.split())
