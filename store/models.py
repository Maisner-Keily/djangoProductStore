from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    shortDescription = models.CharField(max_length=100)
    image = models.CharField(
        max_length=200, default='https://droider.ru/wp-content/uploads/2016/12/parcel-delivery-package.jpg')
    price = models.FloatField()
    bgColor = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    email = models.EmailField()
    name = models.CharField(max_length=50, default='Покупатель')
    effect = models.SmallIntegerField(default=0)
    delivery = models.SmallIntegerField(default=0)

    def __repr__(self):
        return f'{self.id}: {self.title}'