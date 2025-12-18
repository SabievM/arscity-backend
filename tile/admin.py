from django.contrib import admin
from .models import (
    Tile, Material, Country, Category, Purpose, Color, Surface, Form,
    Room, Collection, Pattern, Size, Style, Feature, Slider, Grout, ImageGalary
)

@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'discount', 'is_new', 'is_promo',
        'category', 'material', 'country', 'collection', 'is_large_format'
    )
    search_fields = ('name', 'description')
    list_filter = (
        'is_new', 'is_promo', 'material', 'country', 'purpose',
        'color', 'surface', 'form', 'room', 'collection', 'pattern',
        'size', 'style', 'features', 'is_large_format'
    )
    filter_horizontal = ('purpose', 'features',)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')
    list_filter = ('is_published',)


@admin.register(Grout)
class GroutAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    search_fields = ('name', 'color')

admin.site.register(Material)
admin.site.register(Country)
admin.site.register(Purpose)
admin.site.register(Color)
admin.site.register(Surface)
admin.site.register(Form)
admin.site.register(Room)
admin.site.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name')

admin.site.register(Pattern)
admin.site.register(Size)
admin.site.register(Style)
admin.site.register(Feature)
admin.site.register(Category)
admin.site.register(ImageGalary)