# Generated by Django 5.1.1 on 2024-11-14 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='categories.category'),
            preserve_default=False,
        ),
    ]
