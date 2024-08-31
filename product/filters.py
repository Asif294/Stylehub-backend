


from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    color = filters.CharFilter(field_name='color__name', lookup_expr='iexact')
    size = filters.CharFilter(field_name='size__name', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['category', 'color', 'size']