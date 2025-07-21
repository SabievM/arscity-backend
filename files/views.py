from django.http import FileResponse, HttpResponseNotFound
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PDFDocument
from .serializers import PDFDocumentSerializer
import os

class PDFDocumentListCreateView(generics.ListCreateAPIView):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer

class PDFDownloadView(APIView):
    def get(self, request, pk):
        try:
            pdf = PDFDocument.objects.get(pk=pk)
            if os.path.exists(pdf.file.path):
                response = FileResponse(open(pdf.file.path, 'rb'), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{os.path.basename(pdf.file.name)}"'
                return response
            return HttpResponseNotFound("Файл не найден на сервере")
        except PDFDocument.DoesNotExist:
            return HttpResponseNotFound("Документ не найден")
        

# views.py
class PDFPreviewView(APIView):
    def get(self, request, pk):
        try:
            pdf = PDFDocument.objects.get(pk=pk)
            if os.path.exists(pdf.file.path):
                response = FileResponse(open(pdf.file.path, 'rb'), content_type='application/pdf')
                response['Content-Disposition'] = f'inline; filename="{os.path.basename(pdf.file.name)}"'
                return response
            return HttpResponseNotFound("Файл не найден")
        except PDFDocument.DoesNotExist:
            return HttpResponseNotFound("Документ не найден")