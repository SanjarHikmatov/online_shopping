# Generated by Django 5.1.1 on 2024-11-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0005_alter_featurevalue_feature'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(upload_to='products/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='productfeature',
            name='feature_values',
            field=models.ManyToManyField(related_name='product_features_values', to='features.featurevalue'),
        ),
    ]
