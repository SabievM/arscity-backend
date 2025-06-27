from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TileViewSet, SliderViewSet, GroutViewSet, CollectionViewSet

router = DefaultRouter()
router.register(r'tiles', TileViewSet, basename='tile')
router.register(r'slider', SliderViewSet)
router.register(r'grouts', GroutViewSet)
router.register(r'collections', CollectionViewSet, basename='collection')

urlpatterns = [
    path('', include(router.urls)),
]


