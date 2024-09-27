# Generated by Django 5.1 on 2024-09-25 09:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('gender', models.CharField(choices=[('0', 'MALE'), ('1', 'FEMALE')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SellerSocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_media', models.PositiveSmallIntegerField(choices=[(0, 'Instagram'), (1, 'Telegram')], default=1)),
                ('link', models.URLField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('language', models.CharField(choices=[('EN', 'En'), ('RU', 'Ru')], max_length=10)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.seller')),
            ],
        ),
    ]
