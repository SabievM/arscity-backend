from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="тип товара")
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')
        verbose_name = "Корзина пользователей"
        verbose_name_plural = "Корзины пользователей"


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')

    name = models.CharField(max_length=255)
    image1 = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)
    country = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    number_of_elements = models.PositiveIntegerField(default=1)

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')
        verbose_name = "Избранные товары пользователей"
        verbose_name_plural = "Избранные товары пользователей"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании оплаты'),
        ('paid', 'Оплачено'),
    ]

    DELIVERY_METHOD_CHOICES = [
        ('pickup', 'Самовывоз'),
        ('delivery', 'Доставка на объект'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('office', 'Оплата в офисе'),
        ('online', 'Онлайн оплата'),
        ('courier', 'Оплата курьеру'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='статус')
    payment_receipt_url = models.URLField(blank=True, null=True)

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='email')
    comment = models.TextField(blank=True, null=True, verbose_name='комментарий')

    delivery_method = models.CharField(max_length=20, choices=DELIVERY_METHOD_CHOICES, verbose_name='Способ доставки')
    delivery_address = models.TextField(blank=True, null=True, verbose_name='Адрес доставки')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name='Способ оплаты')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='Общая стоимость')

    class Meta:
        verbose_name = "Заказы пользователя"
        verbose_name_plural = "Заказы пользователей"

    def __str__(self):
        return f"Order #{self.pk} by {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField()