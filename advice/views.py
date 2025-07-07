from rest_framework import viewsets
from .models import Advice
from .serializers import AdviceSerializer

class AdviceViewSet(viewsets.ModelViewSet):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
