from django.db import models

class Supplier(models.Model):
    name = models.TextField()
    phone = models.TextField()
    address = models.TextField()
    email = models.EmailField()
    month = models.TextField()
    
class ProductFamily(models.Model):
    productName = models.TextField()
    unitPrice = models.FloatField()
    stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Product(models.Model):
    productName = models.TextField()
    expirationDate = models.DateField()
    priceAtMoment = models.FloatField()
    ProductFamily = models.ForeignKey(ProductFamily, on_delete=models.CASCADE)

class Client(models.Model):
    name = models.TextField()
    phone = models.TextField()
    adress = models.TextField()
    email = models.EmailField()