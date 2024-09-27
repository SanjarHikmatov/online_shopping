# from django.contrib.auth.models import User
# from django.db import models
#
#
#
#
# class Director(models.Model):
#     name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15)
#
#     def __str__(self):
#         return self.name
#
#
# class Company(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)
#     director = models.OneToOneField(Director, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Scooter(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)
#     scooter_model = models.CharField(max_length=100)
#     feature = models.TextField()
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Service(models.Model):
#     type = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.type
#
#
# class Rental(models.Model):
#     scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rental_type = models.CharField(max_length=50)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#
# class Statistika(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
#     rental_duration = models.IntegerField()
#     services_count = models.IntegerField()
#     payment = models.DecimalField(max_digits=10, decimal_places=2)
#     created_date = models.DateTimeField(auto_now_add=True)
#


