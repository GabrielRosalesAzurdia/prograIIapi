from rest_framework import viewsets
from .serializer import SupplierSerializer, ProductFamilySerializer, ProductSerializer, ClientSerializer
from .models import Supplier, ProductFamily, Product, Client

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class ProductFamilyViewSet(viewsets.ModelViewSet):
    queryset = ProductFamily.objects.all()
    serializer_class = ProductFamilySerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer