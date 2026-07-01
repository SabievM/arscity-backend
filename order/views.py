from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CartItem, Favorite, Order, OrderItem
from .serializers import CartItemSerializer, FavoriteSerializer, OrderSerializer
from django.core.mail import send_mail

class CartItemListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


class CartItemDeleteView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CartTotalPriceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        total = 0.0
        for item in cart_items:
            price = getattr(item.product, 'price', 0.0)
            total += float(price) * item.quantity
        return Response({'total_price': round(total, 2)})


class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


class FavoriteDeleteView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)



class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    

class CreateOrderFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)

        if not cart_items.exists():
            return Response({'detail': 'Cart is empty.'}, status=400)

        data = request.data

        required = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'delivery_method',
            'payment_method'
        ]
        for field in required:
            if not data.get(field):
                return Response({field: 'This field is required.'}, status=400)

        if data['delivery_method'] == 'delivery' and not data.get('delivery_address'):
            return Response(
                {'delivery_address': 'Required for delivery.'},
                status=400
            )

        # 🔹 Подсчёт суммы
        total = 0
        for item in cart_items:
            price = getattr(item.product, 'price', 0)
            total += float(price) * item.quantity

        # 🔹 Создание заказа
        order = Order.objects.create(
            user=user,
            first_name=data['first_name'],
            last_name=data['last_name'],
            patronymic=data.get('patronymic', ''),
            phone=data['phone'],
            email=data['email'],
            comment=data.get('comment', ''),
            delivery_method=data['delivery_method'],
            delivery_address=data.get('delivery_address', ''),
            payment_method=data['payment_method'],
            total_price=total
        )

        # 🔹 Создание позиций заказа
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                content_type=item.content_type,
                object_id=item.object_id,
                quantity=item.quantity
            )

        # 🔹 Отправка email
        items_text = "\n".join([
            f"- {item.product.name} × {item.quantity}"
            for item in cart_items
        ])

        dl = ""
        pyment = ""
        if dl == "delivery" and pyment=="courier":
            dl = "Доставка"
            pyment = "Оплата при получении"
        elif dl == "pickup" and pyment=="office":
            dl = "Самовызов"
            pyment = "В офисе"
        elif dl == "delivery" and pyment!="courier":
            dl = "Доставка"
            pyment = "В офисе"
        else:
            dl = "Самовызов"
            pyment = "Оплата при получении"

        message = f"""
            Новый заказ №{order.id}

            ФИО:
            {order.last_name} {order.first_name} {order.patronymic}

            Телефон: {order.phone}
            Email: {order.email}

            Доставка:
            {dl}
            Адрес: {order.delivery_address or '—'}

            Оплата:
            {pyment}

            Товары:
            {items_text}

            Сумма:
            {order.total_price} ₽

            Комментарий:
            {order.comment or '—'}
        """

        send_mail(
            subject=f'Новый заказ №{order.id}',
            message=message,
            from_email=None,
            recipient_list=['msabieff@yandex.ru'],
            fail_silently=False
        )

        client_message = f"""
            Здравствуйте, {order.first_name}!

            Ваш заказ №{order.id} успешно оформлен.

            Сумма заказа: {order.total_price} ₽

            Способ доставки: {dl}
            Способ оплаты: {pyment}

            В ближайшее время с вами свяжется менеджер для подтверждения заказа.

            Благодарим за заказ!
        """

        send_mail(
            subject=f'Ваш заказ №{order.id} принят',
            message=client_message,
            from_email=None,
            recipient_list=[order.email],
            fail_silently=False
        )

        # 🔹 Очистка корзины
        cart_items.delete()

        return Response(
            {
                "success": True,
                "message": "Заказ оформлен, с вами свяжется менеджер",
                "order": OrderSerializer(order).data
            },
            status=status.HTTP_201_CREATED
        )

