from rest_framework import serializers
from .models import Sell, Receipt

class SellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sell
        fields = '__all__'
        
class ReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipt
        fields = '__all__'
