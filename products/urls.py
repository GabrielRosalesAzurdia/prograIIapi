from django.urls import path , include
from rest_framework import routers
from .views import SupplierViewSet, ProductFamilyViewSet, ProductViewSet, ClientViewSet

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'productFamilies', ProductFamilyViewSet)
router.register(r'products', ProductViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)) ,
]