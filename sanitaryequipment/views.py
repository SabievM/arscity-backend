from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import ShowerAssembly
from .serializers import ProductSerializer
from .serializers import ProductDetailSerializer
from .filters import ProductFilter


# Кастомный класс пагинации (можно переопределить размер страницы)
class ProductPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'  # разрешаем клиенту менять размер через ?
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ShowerAssembly.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination  # подключаем пагинацию

    # Подключаем бэкенды фильтрации
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Указываем наш класс фильтров
    filterset_class = ProductFilter
    
    # Поля для поиска (работает через ?search=запрос)
    search_fields = ['article', 'name', 'manufacturer', 'brand', 'category']
    
    # Поля для сортировки (работает через ?ordering=price или ?ordering=-price)
    ordering_fields = ['price', 'name', 'created_at', 'depth', 'volume', 'stock']
    ordering = ['name']  # сортировка по умолчанию



class ProductRetrieveView(RetrieveAPIView):
    queryset = ShowerAssembly.objects.all()
    serializer_class = ProductDetailSerializer