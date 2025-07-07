import django_filters
from .models import Tile, Grout, Country, Purpose, Color, Surface, Form, Room, Collection, Pattern, Size, Style, Feature
from django_filters.filters import BaseInFilter, CharFilter
from django_filters import rest_framework as filters


class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class TileFilter(django_filters.FilterSet):
    room = NumberInFilter(field_name='room__id', lookup_expr='in')
    material = NumberInFilter(field_name='material__id', lookup_expr='in')
    color = NumberInFilter(field_name='color__id', lookup_expr='in')
    purpose = NumberInFilter(field_name='purpose__id', lookup_expr='in')
    pattern = NumberInFilter(field_name='pattern__id', lookup_expr='in')
    size = NumberInFilter(field_name='size__id', lookup_expr='in')
    style = NumberInFilter(field_name='style__id', lookup_expr='in')
    surface = NumberInFilter(field_name='surface__id', lookup_expr='in')
    form = NumberInFilter(field_name='form__id', lookup_expr='in')
    collection = NumberInFilter(field_name='collection__id', lookup_expr='in')
    country = NumberInFilter(field_name='country__id', lookup_expr='in')
    features = NumberInFilter(field_name='features__id', lookup_expr='in')
    is_new = django_filters.BooleanFilter()
    is_sale = django_filters.BooleanFilter()
    is_large_format = django_filters.BooleanFilter()
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    popularity_score = django_filters.NumberFilter(field_name='popularity_score', lookup_expr='gte')
    tile_type = django_filters.CharFilter(field_name='tile_type', lookup_expr='exact')

    class Meta:
        model = Tile
        fields = []


class CollectionFilter(django_filters.FilterSet):
    popularity_score = django_filters.NumberFilter(field_name='popularity_score', lookup_expr='gte')

    class Meta:
        model = Collection
        fields = ['popularity_score']




class CharInFilter(BaseInFilter, CharFilter):
    pass


class GroutFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    color = django_filters.CharFilter(lookup_expr='icontains')
    type = CharInFilter(field_name='type', lookup_expr='in')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Grout
        fields = [
            'name', 
            'color', 
            'type',
            'price_min',
            'price_max',
        ]