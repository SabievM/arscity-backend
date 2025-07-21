from django.contrib import admin
from django.http import FileResponse
from .models import PDFDocument
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.conf import settings
import os

@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_link', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at', 'preview_link')
    fieldsets = (
        (None, {
            'fields': ('title', 'file')
        }),
        ('Дополнительная информация', {
            'fields': ('preview_link', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def file_link(self, obj):
        if obj.file:
            url = reverse('admin:pdf_download', args=[obj.id])
            return mark_safe(f'<a href="{url}">Скачать</a>')
        return "—"
    file_link.short_description = "Файл"

    def preview_link(self, obj):
        if obj.file:
            url = reverse('admin:pdf_download', args=[obj.id])
            return mark_safe(f'<a href="{url}" target="_blank">Просмотреть PDF</a>')
        return "—"
    preview_link.short_description = "Просмотр"

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('<int:pk>/download/',
                 self.admin_site.admin_view(self.download_pdf),
                 name='pdf_download'),
        ]
        return custom_urls + urls

    def download_pdf(self, request, pk):
        pdf = self.get_object(request, str(pk))
        if os.path.exists(pdf.file.path):
            response = FileResponse(open(pdf.file.path, 'rb'), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf.file.name)}"'
            return response
        from django.http import HttpResponseNotFound
        return HttpResponseNotFound("Файл не найден")