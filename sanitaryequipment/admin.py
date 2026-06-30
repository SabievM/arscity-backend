from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ShowerAssembly
from .resources import ProductResource

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

@admin.register(ShowerAssembly)
class ProductAdmin(ImportExportModelAdmin):
    resource_classes = [ProductResource]
    list_display = ('article', 'name', 'price', 'category', 'manufacturer', 'stock')
    list_filter = ('category', 'manufacturer', 'brand', 'product_type')
    search_fields = ('article', 'name', 'manufacturer', 'brand')

    actions = [send_new, send_sale, send_collection]