# Generated by Django 5.1 on 2024-09-30 13:43

import apps.general.validation_phone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.CharField(help_text='UZB Number +998123456789', max_length=13, validators=[apps.general.validation_phone.validate_phone])),
                ('phone2', models.CharField(blank=True, max_length=13, null=True, validators=[apps.general.validation_phone.validate_phone])),
                ('location', models.URLField()),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(upload_to='general/logo/image/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('icon', models.ImageField(upload_to='social_links/icon/image/%Y/%m/%d/')),
            ],
        ),
    ]
