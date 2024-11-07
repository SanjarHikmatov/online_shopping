from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.contrib.auth.hashers import make_password

from apps.general.service import user_photo_location


class CustomUserManager(UserManager):

    def _create_user(self, email, password, first_name, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields["is_staff"] = extra_fields["is_superuser"] = True
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    photo = models.ImageField(
        upload_to=user_photo_location,
        null=True,
        blank=True
    )


    objects = CustomUserManager()

    user_wishlist_count = models.PositiveSmallIntegerField(default=0)
    user_cart_count = models.PositiveSmallIntegerField(default=0)
    user_comments_count = models.PositiveSmallIntegerField(default=0)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
