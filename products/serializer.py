from rest_framework import serializers
from .models import Supplier, ProductFamily, Product, Client

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'
        
class ProductFamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductFamily
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'