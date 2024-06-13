from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1080)
    slug = models.CharField(max_length=250)
    price = models.FloatField()
    featured = models.BooleanField(default=False)
    images = ArrayField(models.CharField(max_length=1080),
                        blank=True, default=list)
    thumbnail = models.CharField(max_length=2000)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name


class Email_messages(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.TextField(max_length=1440)

    def __str__(self):
        return self.email
