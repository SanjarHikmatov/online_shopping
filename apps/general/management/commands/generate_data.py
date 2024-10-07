import os
# import random

import requests
from random import randint, choice
from faker import Faker

from django.conf import settings
from django.utils.timezone import now
from django.core.management.base import BaseCommand

from apps.abouts.models import About
from apps.categories.models import Category
from apps.products.models import Product
from apps.products.models import CurrencyChoices
from apps.general.service import random_image_url, random_image_download

fake = Faker()

def generate_about():
    today = now().date()

    if not About.objects.exists():
        django_filename = f'abouts/images/{today.year}/{today.month}/{today.day}'

        # ===== check image dir for existing ======
        image_dir = os.path.join(settings.MEDIA_ROOT, django_filename)
        image_name = random_image_download(image_dir)

        About.objects.create(
            title=fake.text(100),
            description=fake.paragraph(500),
            image=os.path.join(django_filename, image_name)
        )
def generate_products():
    today = now().date()
    django_filename = f'products/images/{today.year}/{today.month}/{today.day}'
    image_dir = os.path.join(settings.MEDIA_ROOT, django_filename)


    # for cat_id in range(10):
    category_name = category = Category.objects.create(
      name=fake.first_name(),
    )
    for i in range(100):
        image_name = random_image_download(image_dir)
        print('hello')

        Product.objects.create(
                title=fake.text(255),
                price=randint(1, 100),
                old_price=randint(1, 100),
                currency=choice(CurrencyChoices.choices),
                short_description=fake.text(500),
                long_description=fake.text(500),
                category=category_name,
                main_image=os.path.join(django_filename, image_name)
            )


class Command(BaseCommand):
    def handle(self, *args, **options):
        #====== generate about model ======
        print(self.stdout.write(self.style.SUCCESS('Generating about ........')))
        generate_about()
        # ===== generate products ========
        print(self.stdout.write(self.style.SUCCESS('Generating products ........')))
        generate_products()
        print(self.stdout.write(self.style.SUCCESS('Generating done ........')))
