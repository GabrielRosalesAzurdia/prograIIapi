from django.urls import path , include
from rest_framework import routers
from .views import SellViewSet, ReceiptViewSet

router = routers.DefaultRouter()
router.register(r'sells', SellViewSet)
router.register(r'receipts', ReceiptViewSet)

urlpatterns = [
    path('', include(router.urls)) ,
]