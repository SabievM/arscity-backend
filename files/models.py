from django.db import models
from django.conf import settings
import os

def pdf_upload_path(instance, filename):
    return os.path.join('pdf_files', filename)

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=pdf_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Удаляем файл при удалении записи
        if os.path.isfile(self.file.path):
            os.remove(self.file.path)
        super().delete(*args, **kwargs)