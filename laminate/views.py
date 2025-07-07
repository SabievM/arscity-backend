from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Laminate, Underlay, SkirtingBoard, Grade, Thickness, Chamfer, WaterResistance, LaminatePattern, Tone, WoodType, Gloss, Width, Texture, Construction, ConnectionType
from tile.models import Category, Country
from .serializers import LaminateSerializer, UnderlaySerializer, SkirtingBoardSerializer
from .filters import LaminateFilter, UnderlayFilter, SkirtingBoardFilter
from django.contrib.contenttypes.models import ContentType

class LaminatePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class LaminateViewSet(viewsets.ModelViewSet):
    queryset = Laminate.objects.all()
    serializer_class = LaminateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LaminateFilter
    pagination_class = LaminatePagination

    @action(detail=False, methods=["get"], url_path="filters")
    def filter_options(self, request):
        data = {
            "thickness": {
                "verbose_name": Thickness._meta.verbose_name,
                "items": list(Thickness.objects.values("id", "name"))
            },
            "grades": {
                "verbose_name": Grade._meta.verbose_name,
                "items": list(Grade.objects.values("id", "name"))
            },
            "countries": {
                "verbose_name": Country._meta.verbose_name,
                "items": list(Country.objects.values("id", "name"))
            },
            "chamfers": {
                "verbose_name": Chamfer._meta.verbose_name,
                "items": list(Chamfer.objects.values("id", "name"))
            },
            "water_resistances": {
                "verbose_name": WaterResistance._meta.verbose_name,
                "items": list(WaterResistance.objects.values("id", "name"))
            },
            "laminate_patterns": {
                "verbose_name": LaminatePattern._meta.verbose_name,
                "items": list(LaminatePattern.objects.values("id", "name"))
            },
            "tones": {
                "verbose_name": Tone._meta.verbose_name,
                "items": list(Tone.objects.values("id", "name"))
            },
            "wood_types": {
                "verbose_name": WoodType._meta.verbose_name,
                "items": list(WoodType.objects.values("id", "name"))
            },
            "gloss": {
                "verbose_name": Gloss._meta.verbose_name,
                "items": list(Gloss.objects.values("id", "name"))
            },
            "width": {
                "verbose_name": Width._meta.verbose_name,
                "items": list(Width.objects.values("id", "name"))
            },
            "textures": {
                "verbose_name": Texture._meta.verbose_name,
                "items": list(Texture.objects.values("id", "name"))
            },
            "constructions": {
                "verbose_name": Construction._meta.verbose_name,
                "items": list(Construction.objects.values("id", "name"))
            },
            "connection_types": {
                "verbose_name": ConnectionType._meta.verbose_name,
                "items": list(ConnectionType.objects.values("id", "name"))
            },
        }
        return Response(data)



class UnderlayViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Underlay.objects.all()
    serializer_class = UnderlaySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UnderlayFilter

    @action(detail=False, methods=["get"], url_path="content_type")
    def get_content_type(self, request):
        ct = ContentType.objects.get_for_model(Underlay)
        return Response({
            "app_label": ct.app_label,
            "model": ct.model,
            "id": ct.id,
        })


class SkirtingBoardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SkirtingBoard.objects.all()
    serializer_class = SkirtingBoardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SkirtingBoardFilter

    @action(detail=False, methods=["get"], url_path="content_type")
    def get_content_type(self, request):
        ct = ContentType.objects.get_for_model(SkirtingBoard)
        return Response({
            "app_label": ct.app_label,
            "model": ct.model,
            "id": ct.id,
        })