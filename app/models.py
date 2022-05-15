from django.db import models
from django.db.models.signals import pre_save
from uuid import uuid4
from datetime import timedelta, datetime, timezone
from django.utils import timezone
from django.dispatch import receiver
DILIVERY_PRICE = 20 # right now the dilivery price is harcoded

__all__ = ["Supplier", "Buyer", "Item", "Order"]

# Create your models here.
class Supplier(models.Model):
    id       = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name     = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    phone    = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Buyer(models.Model):
    id       = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name     = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    phone    = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name        = models.CharField(max_length=20)
    quantity    = models.IntegerField(default=1) 
    price       = models.IntegerField(default=20)
    description = models.CharField(max_length=250)
    supplier    = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def is_stock(self) -> bool:
        return self.quantity != 0

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    OUT_OF_STOCK = 1
    ONDILIVERY=  2
    CANCELLED =  3
    DILIVERED =  4
    DELETED   =  6
    DILIVERY_STATUS = [
        (ONDILIVERY, "Order is out for dilivery"),
        (CANCELLED, "Order is cancelled"),
        (DILIVERED, "Order is is dilivered"),
        (OUT_OF_STOCK, "Order amount is more than in stock"),
        (DELETED, "Order is deleted"),
    ]

    ADD_TO_CART = 1
    PURCHASE    = 2
    CANCELL     = 3
    ORDER_STATUS = [
        (ADD_TO_CART, "ADD ITEMS TO CART"),
        (PURCHASE,    "PURCHASE"),
        (CANCELL,     "CANCELL")
    ]

    id             = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    buyer          = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    supplier       = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item           = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity       = models.IntegerField(default=1) 
    departed_date  = models.DateField(default=timezone.now)
    dilivered_date = models.DateField(default=timezone.now)
    action         = models.IntegerField(choices=ORDER_STATUS, default=ADD_TO_CART)
    status         = models.IntegerField(choices=DILIVERY_STATUS, default=OUT_OF_STOCK)
    price          = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.buyer

@receiver(pre_save, sender=Order)
def save_order(sender, instance, **kwargs):
    self=instance
    if self.action == Order.PURCHASE:
        if self.item.quantity <= self.quantity:
            self.status = Order.OUT_OF_STOCK
        else:
            self.item.quantity -= self.quantity
            self.departed_date = datetime.now()
            self.dilivered_date = self.departed_date + timedelta(hours=24)
            self.status = Order.ONDILIVERY
            self.price = ((self.delivered_data - self.departed_date) * DILIVERY_PRICE 
                        + self.quantity * self.item.price)
            instance.item.save()

    elif self.action == Order.CANCELL:
        self.status = Order.DELETED
        self.item.quantity += self.quantity

    # def get_eta(self):
    #     return 

    # def total_amount(self) -> float:
    #     return (
    #         DILIVERY_PRICE * self.get_eta() # dilivery price
    #         + self.quantity * self.item.price  # product price
    #     )



