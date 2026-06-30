from django.contrib import admin
from .models import (
    Laminate, Grade, Thickness, Chamfer, WaterResistance,
    LaminatePattern, Tone, WoodType, Gloss, Width, Texture,
    Construction, ConnectionType, Underlay, SkirtingBoard
)
from newsletter.admin_actions import send_newsletter_action

def send_new(modeladmin, request, queryset):
    return send_newsletter_action(modeladmin, request, queryset, mail_type="new")
send_new.short_description = "🆕 Отправить новинки"


def send_sale(modeladmin, request, queryset):
    return send_newsletter_action(modeladmin, request, queryset, mail_type="sale")
send_sale.short_description = "🔥 Отправить акции"


def send_collection(modeladmin, request, queryset, mail_type="collection"):
    return send_newsletter_action(modeladmin, request, queryset, mail_type="collection")
send_collection.short_description = "📦 Отправить подборку"

@admin.register(Laminate)
class LaminateAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'discount', 'is_promo',
        'grade', 'thickness', 'country', 'chamfer', 'water_resistance'
    )
    search_fields = ('name', 'description')
    list_filter = (
        'is_promo', 'grade', 'thickness', 'country', 'chamfer',
        'water_resistance', 'laminate_pattern', 'tone', 'wood_type', 'gloss',
        'width', 'texture', 'is_substrate', 'construction', 'connection_type'
    )
    actions = [send_new, send_sale, send_collection]

@admin.register(Underlay)
class UnderlayAdmin(admin.ModelAdmin):
    list_display = ('thickness', 'has_vapor_barrier', 'floor_type')
    list_filter = ('thickness', 'has_vapor_barrier', 'floor_type')
    actions = [send_new, send_sale, send_collection]


@admin.register(SkirtingBoard)
class SkirtingBoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'thickness', 'height', 'moisture_resistance', 'tone')
    list_filter = ('type', 'moisture_resistance', 'tone')
    search_fields = ('name',)
    actions = [send_new, send_sale, send_collection]

admin.site.register(Grade)
admin.site.register(Thickness)
admin.site.register(Chamfer)
admin.site.register(WaterResistance)
admin.site.register(LaminatePattern)
admin.site.register(Tone)
admin.site.register(WoodType)
admin.site.register(Gloss)
admin.site.register(Width)
admin.site.register(Texture)
admin.site.register(Construction)
admin.site.register(ConnectionType)