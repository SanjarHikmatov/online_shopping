from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])



