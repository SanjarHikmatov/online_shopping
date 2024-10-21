# Generated by Django 5.1 on 2024-10-21 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_uz', models.CharField(max_length=100, null=True)),
                ('title_ru', models.CharField(max_length=100, null=True)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=500)),
                ('description_uz', models.CharField(max_length=500, null=True)),
                ('description_ru', models.CharField(max_length=500, null=True)),
                ('description_en', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='abouts/images/%Y/%m/%d/')),
            ],
        ),
    ]
