from django.db import models

class ProductFeatures(models.Model):
    product = models.ForeignKey(to='projects.Product', on_delete=models.CASCADE)
    feature_value = models.ForeignKey('features.FeatureValue', on_delete=models.CASCADE)