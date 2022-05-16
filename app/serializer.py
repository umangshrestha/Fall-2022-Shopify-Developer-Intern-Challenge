from datetime import datetime
from rest_framework import fields, serializers
from .models import *
from rest_framework.permissions import DjangoModelPermissions

__all__ = ["ItemSerializer", "WarehouseSerializer", "TrashSerializer"]

class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Warehouse
        fields = ("id", "name", "location", "phone")


class ItemSerializer(serializers.ModelSerializer):
    supplier = WarehouseSerializer
    class Meta:
        model  = Item
        fields = ("id", "name", "quantity", "price_per_item", "description", "warehouse")

class TrashSerializer(serializers.ModelSerializer):
    supplier = WarehouseSerializer
    class Meta:
        model  = Item
        fields = ("id", "name", "quantity", "price_per_item", "description", "warehouse", "is_deleted")
