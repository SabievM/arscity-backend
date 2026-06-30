from django_filters import rest_framework as filters
from .models import ShowerAssembly

class ProductFilter(filters.FilterSet):
    # Кастомные фильтры для числовых диапазонов (цена, размеры)
    price_min = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="price", lookup_expr='lte')
    
    length_min = filters.NumberFilter(field_name="length_mm", lookup_expr='gte')
    length_max = filters.NumberFilter(field_name="length_mm", lookup_expr='lte')
    
    # Фильтр по наличию остатков (> 0)
    in_stock = filters.BooleanFilter(method='filter_in_stock')
    
    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset

    class Meta:
        model = ShowerAssembly
        fields = {
            # Точные совпадения
            'article': ['exact'],
            'category': ['exact'],
            'manufacturer': ['exact'],
            'brand': ['exact'],
            'product_type': ['exact'],
            'material': ['exact'],
            'mounting_type': ['exact'],
            'flush_type': ['exact'],
            'has_shelf': ['exact'],
            'rimless': ['exact'],
            'seat_lift': ['exact'],
            # Частичные совпадения (содержит подстроку)
            'name': ['icontains'],
            # Числовые диапазоны (можно будет использовать ?depth=50)
            'depth': ['exact', 'gte', 'lte'],
            'volume': ['exact', 'gte', 'lte'],
            'price': ['exact', 'gte', 'lte'],
        }