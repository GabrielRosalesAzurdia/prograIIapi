from django.db import models

class Supplier(models.Model):
    name = models.TextField()
    phone = models.TextField()
    address = models.TextField()
    email = models.EmailField()
    month = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
class ProductFamily(models.Model):
    productName = models.TextField()
    unitPrice = models.FloatField()
    stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "Family " + self.productName
class Product(models.Model):
    productName = models.TextField()
    expirationDate = models.DateField()
    priceAtMoment = models.FloatField()
    ProductFamily = models.ForeignKey(ProductFamily, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.productName
class Client(models.Model):
    name = models.TextField()
    phone = models.TextField()
    adress = models.TextField()
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.name