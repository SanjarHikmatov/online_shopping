import os
import random

from django.db import transaction
from faker import Faker

from django.conf import settings
from django.utils.timezone import now
from django.core.management.base import BaseCommand

from apps.abouts.models import About
from apps.categories.models import Category
from apps.products.models import Product
from apps.general.models import General
from apps.general.service import random_image_url, random_image_download

fake = Faker()
class Command(BaseCommand):
    @staticmethod
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
    @staticmethod
    def generate_products():
        today = now().date()
        django_filename = f'products/images/{today.year}/{today.month}/{today.day}'
        image_dir = os.path.join(settings.MEDIA_ROOT, django_filename)
        image_name = random_image_download(image_dir)
        counts = 100
        for cat_name in range(10):
            print(counts)
            category = Category.objects.create(
              name=fake.first_name(),
              category_image=os.path.join(django_filename,image_name )
            )
            if cat_name % 2:
                for i in range(3):
                    Category.objects.create(name=fake.first_name(), parent_id=category.pk)
            #============== create child ==============
            products = []

            for i in range(100):
                counts += 1
                products.append(
                    Product(
                        title=fake.text(255),
                        price=random.randint(5, 500),
                        old_price=random.randint(500, 1000),
                        currency=random.choice(General.CurrencyChoices.choices)[0],
                        short_description=fake.text(500),
                        long_description=fake.text(500),
                        category_id=category.pk,
                        main_image=os.path.join(django_filename, image_name),
                    )
                )

            Product.objects.bulk_create(products)

    @transaction.atomic
    def handle(self, *args, **options):
        #====== generate about model ======
        print(self.stdout.write(self.style.SUCCESS('Generating about ........')))
        self.generate_about()
        # ===== generate products ========
        print(self.stdout.write(self.style.SUCCESS('Generating products ........')))
        self.generate_products()
        print(self.stdout.write(self.style.SUCCESS('Generating done ........')))
