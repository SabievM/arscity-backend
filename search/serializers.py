from rest_framework import serializers
from tile.models import Tile, Grout, Country
from laminate.models import Laminate, Underlay, SkirtingBoard
from sanitaryequipment.models import ShowerAssembly

# Сериализатор для плитки (Tile)
class SimpleTileSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name', default=None)

    class Meta:
        model = Tile
        fields = ['id', 'name', 'price', 'image1', 'tile_type', 'country']


# Сериализатор для ламината (Laminate)
class SimpleLaminateSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name', default=None)

    class Meta:
        model = Laminate
        fields = ['id', 'name', 'price', 'image1', 'country']


# Сериализатор для подложек (Underlay)
class SimpleUnderlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Underlay
        fields = ['id', 'name', 'price', 'image1']


# Сериализатор для плинтусов (SkirtingBoard)
class SimpleSkirtingBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkirtingBoard
        fields = ['id', 'name', 'price', 'image1']


# Сериализатор для затирки (Grout)
class SimpleGroutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grout
        fields = ['id', 'name', 'color', 'price', 'image1']

class SimpleShowerAssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowerAssembly
        fields = ['id', 'name',  'price', 'image1'] 