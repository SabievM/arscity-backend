from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from tile.models import Tile, Grout
from laminate.models import Laminate, Underlay, SkirtingBoard
from sanitaryequipment.models import ShowerAssembly
from .serializers import (
    SimpleTileSerializer,
    SimpleLaminateSerializer,
    SimpleUnderlaySerializer,
    SimpleSkirtingBoardSerializer,
    SimpleGroutSerializer,
    SimpleShowerAssemblySerializer
)


class GlobalSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        results = []

        if query:
            tiles = Tile.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            results.extend([
                {"type": "tile", **item} for item in SimpleTileSerializer(tiles, many=True).data
            ])

            laminates = Laminate.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            results.extend([
                {"type": "laminate", **item} for item in SimpleLaminateSerializer(laminates, many=True).data
            ])

            underlays = Underlay.objects.filter(Q(name__icontains=query))
            results.extend([
                {"type": "underlay", **item} for item in SimpleUnderlaySerializer(underlays, many=True).data
            ])

            skirting_boards = SkirtingBoard.objects.filter(Q(name__icontains=query))
            results.extend([
                {"type": "skirting_board", **item} for item in SimpleSkirtingBoardSerializer(skirting_boards, many=True).data
            ])

            grouts = Grout.objects.filter(Q(name__icontains=query) | Q(color__icontains=query))
            results.extend([
                {"type": "grout", **item} for item in SimpleGroutSerializer(grouts, many=True).data
            ])
            shower_assemblies = ShowerAssembly.objects.filter(
                Q(name__icontains=query) |
                Q(article__icontains=query) |
                Q(brand__icontains=query) |
                Q(category__icontains=query)
            )
            results.extend([
                {"type": "showerassembly", **item} for item in SimpleShowerAssemblySerializer(shower_assemblies, many=True).data
            ])

        return Response(results)