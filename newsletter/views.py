from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Subscriber
from django.http import HttpResponse


class SubscribeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        email = request.data.get("email")

        Subscriber.objects.get_or_create(
            email=email
        )

        return Response({
            "success": True
        })
    


def unsubscribe_view(request, token):
    try:
        subscriber = Subscriber.objects.get(
            unsubscribe_token=token
        )

        subscriber.is_active = False
        subscriber.save()

        return HttpResponse(
            "Вы успешно отписались от рассылки."
        )

    except Subscriber.DoesNotExist:
        return HttpResponse(
            "Ссылка недействительна.",
            status=404
        )