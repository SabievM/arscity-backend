from rest_framework import serializers
from .models import PDFDocument
import os

class PDFDocumentSerializer(serializers.ModelSerializer):
    filename = serializers.SerializerMethodField()
    
    class Meta:
        model = PDFDocument
        fields = ['id', 'title', 'file', 'filename', 'created_at']
    
    def get_filename(self, obj):
        return os.path.basename(obj.file.name) if obj.file else None