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


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    login = models.CharField(max_length=100)
    passwordHash = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ' + self.phone


class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Promocode(models.Model):
    promocode = models.CharField(max_length=50)
    discountPercent = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    isUsed = models.BooleanField(default=False)

    def __str__(self):
        return self.promocode + ' ' + self.discountPercent + ' - ' + ('Использован' if self.isUsed else 'Не использован') 


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=150)
    price = models.FloatField()
    finalPrice = models.FloatField()
    isPayed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.firstName + ' ' + self.user.lastName + ' - ' + ('Оплачен' if self.isPayed else 'Не оплачен')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


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