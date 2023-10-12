from rest_framework import viewsets
from .serializer import SellSerializer, ReceiptSerializer
from .models import Sell, Receipt

class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    
class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer