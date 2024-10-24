from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



class FeatureValue(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = (('feature', 'name'),)

    def __str__(self):
        return self.name
