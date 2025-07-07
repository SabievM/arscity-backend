from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Tile, Slider, Grout, Category, Material, Purpose, Color, Country, Collection, Room, Form, Size, Surface, Style, Pattern, Feature
from .serializers import TileSerializer, SliderSerializer, GroutSerializer, CollectionListSerializer, CollectionDetailGroupedSerializer
from .filters import TileFilter, CollectionFilter, GroutFilter

class TilePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TileFilter
    pagination_class = TilePagination

    @action(detail=False, methods=["get"], url_path="filters")
    def filter_options(self, request):
        data = {
            "categories": list(Category.objects.values("id", "name")),
            "materials": list(Material.objects.values("id", "name")),
            "purposes": list(Purpose.objects.values("id", "name")),
            "colors": list(Color.objects.values("id", "name")),
            "countries": list(Country.objects.values("id", "name")),
            "collections": list(Collection.objects.values("id", "name")),
            "rooms": list(Room.objects.values("id", "name")),
            "shapes": list(Form.objects.values("id", "name")),
            "sizes": list(Size.objects.values("id", "name")),
            "surfaces": list(Surface.objects.values("id", "name")),
            "styles": list(Style.objects.values("id", "name")),
            "patterns": list(Pattern.objects.values("id", "name")),
            "features": list(Feature.objects.values("id", "name")),
        }
        return Response(data)




class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collection.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = CollectionFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CollectionDetailGroupedSerializer
        return CollectionListSerializer



class SliderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Slider.objects.filter(is_published=True)
    serializer_class = SliderSerializer


class GroutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Grout.objects.all()
    serializer_class = GroutSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GroutFilter

