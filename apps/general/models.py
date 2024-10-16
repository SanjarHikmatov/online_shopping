from datetime import timezone

import requests
from django.core.cache import cache
from django.db import models
from django.utils.timezone import now

from .validation_phone import uzb_phone_number_validators
from django.core.exceptions import ValidationError


class General(models.Model):

    class CurrencyChoices(models.TextChoices):
        USD = 'USD', 'USD'
        EUR = 'EUR', 'EUR'
        JPY = 'JPY', 'JPY'
        UZS = 'UZS', 'UZS'

    DEFAULT_CURRENCY = CurrencyChoices.UZS

    phone1 = models.CharField(
        max_length=13,
        validators=[uzb_phone_number_validators],
        help_text="UZB Number +998123456789"
    )
    phone2 = models.CharField(
        max_length=13,
        null=True,
        blank=True,
        validators=[uzb_phone_number_validators]
    )

    location = models.URLField()
    address = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    logo = models.ImageField(upload_to="general/logo/image/%Y/%m/%d/")

    def clean(self):
        if self.pk and General.objects.exists():
            raise ValidationError('Unique')


class GeneralSocialMedia(models.Model):
    url = models.URLField()
    icon = models.ImageField(upload_to="social_links/icon/image/%Y/%m/%d/")


class CurrencyAmount(models.Model):
    GET_CURRENCY_URL = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/{currency}/{date}/"

    currency = models.CharField(max_length=10, choices=General.CurrencyChoices.choices)
    usd_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


    @classmethod
    def get_currency(cls, currency: str):
        today = now().today()
        amount_in_uzs = cache.get(currency)
        if not amount_in_uzs:

            obj, create = cls.objects.get_or_create(
                currency=currency,
                date=today,
                )
            if create:
                obj.usd_amount = requests.get(url=cls.GET_CURRENCY_URL.format(
                        currency=currency,
                        date=today
                    )).json()[0]["Rate"],
                obj.save()
            cache.set(currency, obj.usd_amount)
            amount_in_uzs = cache.get(currency)

        return amount_in_uzs

    class Meta:
        unique_together = (('currency', 'date'),)