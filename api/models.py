from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1080)
    slug = models.CharField(max_length=150)
    price = models.FloatField()
    featured = models.BooleanField(default=False)
    images = models.JSONField(blank=True, default=[])
    thumbnail = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
