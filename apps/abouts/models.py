from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    image = models.ImageField(upload_to='abouts/images/%Y/%m/%d/')


class SocialMedia(models.Model):

    logo = models.ImageField(upload_to='abouts/logo/images/%Y/%m/%d/')
    social_media = models.URLField(max_length=255, unique=True)



