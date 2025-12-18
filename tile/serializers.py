from rest_framework import serializers
from .models import (
    Tile, Material, Country, Purpose, Color, Surface, Form,
    Room, Collection, Pattern, Size, Style, Feature, Slider, Grout, ImageGalary
)

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ['id', 'name']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']

class SurfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surface
        fields = ['id', 'name']

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'name']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']



class CollectionListSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    class Meta:
        model = Collection
        fields = '__all__'

class CollectionDetailGroupedSerializer(serializers.ModelSerializer):
    tiles_by_type = serializers.SerializerMethodField()
    country = serializers.StringRelatedField()
    class Meta:
        model = Collection
        fields = '__all__'

    def get_tiles_by_type(self, obj):
        grouped = {}
        tile_types = dict(Tile.TILE_TYPES).keys()
        for tile_type in tile_types:
            tiles = obj.tiles.filter(tile_type=tile_type)
            grouped[tile_type] = SimpleTileSerializer(tiles, many=True).data
        return grouped

class CollectionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'logo']

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = ['id', 'name']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ['id', 'name']

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name']

class TileSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    material = MaterialSerializer()
    purpose = PurposeSerializer()
    color = ColorSerializer()
    collection = CollectionSimpleSerializer()
    room = RoomSerializer()
    form = FormSerializer()
    size = SizeSerializer()
    surface = SurfaceSerializer()
    style = StyleSerializer()
    pattern = PatternSerializer()

    class Meta:
        model = Tile
        fields = '__all__'

class SimpleTileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = ['id', 'name', 'price', 'image1', 'tile_type']

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'title', 'description', 'image', 'is_published']


class GroutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grout
        fields = '__all__'

class ImageGalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGalary
        fields = ["id", "name", "image"]