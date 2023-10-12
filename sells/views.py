from rest_framework import viewsets, permissions
from .serializer import SellSerializer, ReceiptSerializer
from .models import Sell, Receipt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from products.models import Product, ProductFamily
from products.serializer import ProductSerializer, ProductFamilySerializer

import json

# This one will create empty carts, and delete them and 
# show them both list and by id
class SellViewSet(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    
class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    
# Gets a sell given a sellid, productFamilyid and clientId, specially it has to be on a sutatus True
# Creates a product out of a productFamily
# Puts the product inside of the sell
# updates costs

# @csrf_exempt

@api_view(['PUT'])
@permission_classes((permissions.IsAuthenticated,))
def addItemCart(request,sellid,productFamilyid,clientid):
    
    try:
        sell = Sell.objects.get(pk=sellid, client = clientid, status=True)
        sellArray = json.loads(sell.products)
        productFamily = ProductFamily.objects.get(pk = productFamilyid)
        product = Product(productName = productFamily.productName, priceAtMoment = productFamily.unitPrice, ProductFamily = productFamily)
        product.save()
        serialized_product = ProductSerializer(product)
        sellArray.append(serialized_product.data)
        sell.costs = 0
        for product in sellArray:
            sell.costs = sell.costs + product["priceAtMoment"]
        sell.products = json.dumps(sellArray)
        sell.save()
        serialized_sell = SellSerializer(sell)
        return Response(serialized_sell.data)
    except Sell.DoesNotExist:
        return Response("No cart exists")
    

# Gets a sell given a sellid, productFamilyid and clientId, specially it has to be on a sutatus True
# searches an product by id
# deletes that product from the array and from the database
# updates costs

@api_view(['DELETE'])
@permission_classes((permissions.IsAuthenticated,))
def deleteItemCart(request,sellid,productid,clientid):
    try:
        sell = Sell.objects.get(pk=sellid, client = clientid, status=True)
        sellArray = json.loads(sell.products)
        sell.costs = 0
        for product in sellArray:
            sell.costs = sell.costs + product["priceAtMoment"]
            if product["id"] == productid:
                try:
                    product_to_delete = Product.objects.get(pk=productid)
                    product_to_delete.delete()
                    sellArray.pop(sellArray.index(product))
                except Product.DoesNotExist:
                    return Response("product does not exists")         
        sell.products = json.dumps(sellArray)
        sell.save()
        serialized_sell = SellSerializer(sell)
        return Response(serialized_sell.data)      
    except Sell.DoesNotExist:
        return Response("Sell object does not exist")
    
# Creates a receipt
# sets the sell status as False

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def createReceipt(request,sellid,productid,clientid):
    pass