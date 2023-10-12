from django.urls import path , include
from rest_framework import routers
from .views import SellViewSet, ReceiptViewSet, addItemCart,deleteItemCart

router = routers.DefaultRouter()
router.register(r'sells', SellViewSet)
router.register(r'receipts', ReceiptViewSet)

urlpatterns = [
    path('additemcart/<int:sellid>/<int:productFamilyid>/<int:clientid>', addItemCart) ,
    path('deleteitemcart/<int:sellid>/<int:productid>/<int:clientid>', deleteItemCart) ,
    path('', include(router.urls)) ,
]