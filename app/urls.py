from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'items', ItemsViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'buyers', BuyerViewSet)
router.register(r'orders', OrderViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]