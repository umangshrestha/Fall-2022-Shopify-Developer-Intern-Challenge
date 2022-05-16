from django.db import models
from django.db.models.signals import pre_save
from uuid import uuid4
from datetime import timedelta, datetime, timezone
from django.utils import timezone
from django.dispatch import receiver

__all__ = ["Warehouse", "Item"]

class Warehouse(models.Model):
    id       = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    phone    = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=20)
    quantity    = models.IntegerField() 
    price_per_item  = models.IntegerField()
    description     = models.CharField(max_length=250, default="")
    warehouse_id    = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    is_deleted  = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
