import django_filters
from .models import Item

class ItemFilter(django_filters.FilterSet):   
    queryset = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name
    class Meta:
        model = Item
        fields = '__all__'