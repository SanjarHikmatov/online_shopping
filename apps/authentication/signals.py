from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from apps.abouts.models import About


@receiver(user_login_failed, sender=get_user_model())
def send_message_on_user_login_failed(credentials, request, *args, **kwargs):
    """on login_failed send message to user email"""
    print("tinchlikmi")
    print(args)