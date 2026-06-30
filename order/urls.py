from django.urls import path
from .views import (
    CartItemListCreateView, CartItemDeleteView, CartTotalPriceView,
    FavoriteListCreateView, FavoriteDeleteView,
    CreateOrderFromCartView, OrderListView, CreateOrderFromCartView
)

urlpatterns = [
    path('cart/', CartItemListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:pk>/', CartItemDeleteView.as_view(), name='cart-delete'),
    path('cart/total/', CartTotalPriceView.as_view(), name='cart-total-price'),

    path('favorites/', FavoriteListCreateView.as_view(), name='favorite-list-create'),
    path('favorites/<int:pk>/', FavoriteDeleteView.as_view(), name='favorite-delete'),

    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', CreateOrderFromCartView.as_view(), name='order-create'),
]


