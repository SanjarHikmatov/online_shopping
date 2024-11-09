from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(to='self',
                               null=True,
                               blank=True,
                               related_name='children',
                               on_delete=models.CASCADE,
                               related_query_name='category'
                               )
    category_image = models.ImageField(upload_to='categories/images/%Y/%m/%d')


    def clean(self):
        try:
            if not self.pk and self.parent.parent:
                raise ValidationError('you can creat only three category')
        except AttributeError:
            pass

    def __str__(self):
        return self.name
