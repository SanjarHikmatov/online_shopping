from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=255)



class FeatureValue(models.Model):
    feature = models.ForeignKey('Feature', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)