from django.db import models
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    email = models.EmailField()
    user_subject = models.CharField(max_length=500)
    user_message = models.CharField(max_length=500)


    def __str__(self):
        return self.first_name

