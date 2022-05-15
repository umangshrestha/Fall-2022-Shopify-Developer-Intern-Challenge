from datetime import datetime
from rest_framework import fields, serializers
from .models import *


__all__ = ["ItemSerializer", "SupplierSerializer", "OrderSerializer", "BuyerSerializer"]


class BuyerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Buyer
        fields = ("name", "location", "phone")

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Supplier
        fields = ("name", "location", "phone")


class ItemSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer
    class Meta:
        model  = Item
        fields = ("name", "quantity", "price", "description", "supplier")
        
class OrderSerializer(serializers.ModelSerializer):



    supplier = SupplierSerializer
    buyer = BuyerSerializer
    item = ItemSerializer
    action = serializers.ChoiceField(choices=Order.ORDER_STATUS, write_only=True)
    price = serializers.IntegerField(read_only=True)
    departed_date = serializers.DateField(format="%Y-%m-%d", read_only=True)
    dilivered_date = serializers.DateField(format="%Y-%m-%d", read_only=True)
  
    class Meta:
        model  = Order
        fields = ("buyer", "supplier", "item", "quantity", "departed_date", "dilivered_date", "action", "get_status_display", "price")
       

