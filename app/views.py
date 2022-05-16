from django.shortcuts import render
from rest_framework import  viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .models import * 
from .serializer import *

class ItemList(generics.ListAPIView):
    queryset = Item.objects.filter(is_deleted=False)
    serializer_class = ItemSerializer

class DeletedItemList(generics.ListAPIView):
    queryset = Item.objects.filter(is_deleted=True)
    serializer_class = ItemSerializer

class WarehouseList(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.filter(is_deleted=False)
    serializer_class = ItemSerializer

# class TrashDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Item.objects.filter(is_deleted=True)
#     serializer_class = ItemSerializer

class WarehouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# class TrashDetail(viewsets.ModelViewSet):
#     queryset = Item.objects.filter(is_deleted=True)
#     serializer_class = TrashSerializer

