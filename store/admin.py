from django.contrib import admin
from .models import Category, Product, Promocode, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Promocode)
admin.site.register(Order)
