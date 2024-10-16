from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.contrib.auth.hashers import make_password


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='users/photos/%Y/%m/%d/', null=True, blank=True)

    objects = CustomUserManager()
    wishlist_count = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
