from django.db import models
from django.contrib.auth import get_user_model
from products.models import Client

class Sell(models.Model):
    products = models.TextField()
    costs = models.IntegerField()
    
class Receipt(models.Model):
    employee = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    totalCost = models.IntegerField()
    date = models.DateField(auto_now=True)