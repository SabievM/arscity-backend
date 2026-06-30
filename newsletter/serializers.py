from rest_framework import serializers
from .models import Subscriber

class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = ["email"]