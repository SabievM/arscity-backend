from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductRetrieveView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('sanitaryequipment/', include(router.urls)),
    path('sanitaryequipment/product-detail/<int:pk>/', ProductRetrieveView.as_view(), name='product-detail'),
]