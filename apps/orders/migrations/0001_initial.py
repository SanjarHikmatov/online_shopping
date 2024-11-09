# Generated by Django 5.1.1 on 2024-11-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('paid_at', models.DateTimeField(auto_now_add=True)),
                ('coupon_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_code', models.CharField(max_length=20)),
            ],
        ),
    ]
