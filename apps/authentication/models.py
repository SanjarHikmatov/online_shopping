from django.db import models


from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='users/photos/%Y/%m/%d/', blank=True)