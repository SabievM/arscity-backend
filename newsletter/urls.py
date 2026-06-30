from django.urls import path
from .views import SubscribeView, unsubscribe_view

urlpatterns = [
    path(
        "subscribe/",
        SubscribeView.as_view()
    ),
    path(
    "unsubscribe/<uuid:token>/",
    unsubscribe_view,
    name="unsubscribe"
)
]