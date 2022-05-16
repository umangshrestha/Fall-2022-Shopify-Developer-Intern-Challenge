from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter

from .views import * 

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'warehouse', WarehouseViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path(r'', lambda _ : redirect("/items")),
    # path(r'trash/', DeletedItemList.as_view()),
    # path(r'warehouse/', WarehouseList.as_view()),
    path(r'warehouse/<int:pk>', WarehouseDetail.as_view()),
    path(r'items/<int:pk>', ItemDetail.as_view()),
    # path(r'trash/<int:id>', ItemDetail.as_view()),
    path(r'', include(router.urls), name="add items or warehouse"),
]