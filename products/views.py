from rest_framework import viewsets, permissions
from .serializer import SupplierSerializer, ProductFamilySerializer, ProductSerializer, ClientSerializer
from .models import Supplier, ProductFamily, Product, Client
from sells.models import Receipt
from sells.serializer import ReceiptSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
#from django.views.decorators.csrf import csrf_exempt

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
    
# Gets a client related receipts
# @csrf_exempt
@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def clientReceipts(request,client):
    queryset = Receipt.objects.filter(client = client)
    serializer = ReceiptSerializer(queryset, many=True)
    return Response(serializer.data)