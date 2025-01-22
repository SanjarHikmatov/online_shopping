# Generated by Django 5.1.1 on 2024-11-16 09:32

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('avg_rating', models.DecimalField(decimal_places=1, default=Decimal('0'), editable=False, max_digits=10)),
                ('comment_count', models.DecimalField(decimal_places=1, default=Decimal('0'), editable=False, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Enter the price of the UZS', max_digits=10)),
                ('old_price', models.DecimalField(decimal_places=2, default=0, help_text='Enter the old price of the UZS', max_digits=10)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('RUB', 'RUB'), ('UZS', 'UZS')], default='UZS', max_length=5)),
                ('short_description', models.CharField(max_length=500)),
                ('short_description_uz', models.CharField(max_length=500, null=True)),
                ('short_description_ru', models.CharField(max_length=500, null=True)),
                ('short_description_en', models.CharField(max_length=500, null=True)),
                ('long_description', models.TextField(max_length=500)),
                ('long_description_uz', models.TextField(max_length=500, null=True)),
                ('long_description_ru', models.TextField(max_length=500, null=True)),
                ('long_description_en', models.TextField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('main_image', models.ImageField(upload_to='products/images/%Y/%m/%d/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='categories.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter in UZS', max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, help_text='Enter in UZS', max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('feature_values', models.ManyToManyField(related_name='product_features_values', to='features.featurevalue')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_features', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images/%Y/%m/%d/')),
                ('ordering_number', models.PositiveSmallIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
        ),
    ]
