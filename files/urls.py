from django.urls import path
from .views import PDFDocumentListCreateView, PDFDownloadView, PDFPreviewView

urlpatterns = [
    path('pdf/', PDFDocumentListCreateView.as_view(), name='pdf-list-create'),
    path('pdf/<int:pk>/download/', PDFDownloadView.as_view(), name='pdf-download'),
    path('pdf/<int:pk>/preview/', PDFPreviewView.as_view(), name='pdf-preview'),
]