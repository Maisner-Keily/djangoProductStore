from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=50)
    parentCategory = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.CharField(
        max_length=200, default='https://droider.ru/wp-content/uploads/2016/12/parcel-delivery-package.jpg')
    price = models.FloatField()
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

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
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' ' + self.phone


class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)


class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, default='Россия')
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=10)
    entrance = models.CharField(max_length=10, blank=True)
    apartment = models.CharField(max_length=10, blank=True)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.country + ' ,' + self.city + ' ,' + self.street + ' ' + self.house + ' ,' + self.house + ' ' + self.apartment


class Promocode(models.Model):
    promocode = models.CharField(max_length=50)
    discountPercent = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    isUsed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.promocode + ' ' + self.discountPercent + ' - ' + ('Использован' if self.isUsed else 'Не использован') 


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    finalPrice = models.FloatField()
    isPayed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.firstName + ' ' + self.user.lastName + ' - ' + ('Оплачен' if self.isPayed else 'Не оплачен')


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)


class RecomendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(default=timezone.now)
