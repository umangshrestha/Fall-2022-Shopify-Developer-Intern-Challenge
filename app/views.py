from django.shortcuts import render
from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .models import * 
from .serializer import *

__all__ = ["ItemsViewSet", "SupplierViewSet", "OrderViewSet", "BuyerViewSet"]

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer



