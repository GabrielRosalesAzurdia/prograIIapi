from django.contrib import admin
from .models import Supplier, Client, Product, ProductFamily

admin.site.register(Supplier)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(ProductFamily)