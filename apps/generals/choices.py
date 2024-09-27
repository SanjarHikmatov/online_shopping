from django.db.models import IntegerChoices


class SocialMedia(IntegerChoices):
    INSTAGRAM = 0, 'Instagram'
    TELEGRAM = 1, 'Telegram'
