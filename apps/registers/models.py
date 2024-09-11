from django.core.exceptions import ValidationError
from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)


    def clean(self):
        try:
            if self.password != self.confirm_password or self.pk :
                raise ValidationError('Passwords do not match')
        except ValidationError:
            print('passwords do not match')