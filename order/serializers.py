from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import CartItem, Favorite, Order, OrderItem

class GenericProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.FloatField()



class CartItemSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(write_only=True)
    content_type_display = serializers.SerializerMethodField(read_only=True)
    object_id = serializers.IntegerField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = [
            'id',
            'content_type',
            'content_type_display',
            'object_id',
            'quantity',
            'product'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        model_name = validated_data.pop('content_type').lower()
        object_id = validated_data['object_id']
        quantity = validated_data['quantity']

        try:
            content_type = ContentType.objects.get(model=model_name)
        except ContentType.DoesNotExist:
            raise serializers.ValidationError({
                'content_type': f"Model '{model_name}' not found."
            })

        cart_item, created = CartItem.objects.get_or_create(
            user=user,
            content_type=content_type,
            object_id=object_id,
            defaults={'quantity': quantity}
        )

        if not created and cart_item.quantity != quantity:
            cart_item.quantity = quantity
            cart_item.save(update_fields=['quantity'])

        return cart_item

    def get_content_type_display(self, obj):
        return obj.content_type.model

    # # def get_product(self, obj):
    #     product = obj.product

    #     if not product:
    #         return None

    #     image = ''

    #     if getattr(product, 'image1', None):
    #         try:
    #             # Для ImageField
    #             image = product.image1.url
    #         except AttributeError:
    #             # Для URLField / CharField
    #             image = str(product.image1)

    #     elif getattr(product, 'photos', None):
    #         image = str(product.photos)

    #     return {
    #         'id': product.id,
    #         'name': str(getattr(product, 'name', '')),
    #         'image1': image,
    #         'price': float(getattr(product, 'price', 0) or 0),
    #         'country': str(getattr(product, 'country', '')),
    #         'collection': str(getattr(product, 'collection', ''))
    #         if getattr(product, 'collection', None) else '',
    #     }

    def get_product(self, obj):
        product = obj.product

        if not product:
            return None

        image = ''

        if getattr(product, 'image1', None):
            try:
                image = product.image1.url
            except AttributeError:
                image = str(product.image1)

        elif getattr(product, 'photos', None):
            image = str(product.photos).split("|")[0]

        return {
            'id': product.id,
            'name': str(getattr(product, 'name', '')),
            'image1': image,
            'price': float(getattr(product, 'price', 0) or 0),
            'country': str(getattr(product, 'country', '')),
            'collection': str(getattr(product, 'collection', ''))
            if getattr(product, 'collection', None) else '',
        }



class FavoriteSerializer(serializers.ModelSerializer):
    content_type = serializers.CharField(write_only=True)
    content_type_display = serializers.SerializerMethodField(read_only=True)
    object_id = serializers.IntegerField()

    class Meta:
        model = Favorite
        fields = [
            'id',
            'content_type',
            'content_type_display',
            'object_id',
            'name',
            'image1',
            'price',
            'country',
            'description',
            'number_of_elements',
            'added_at'
        ]
        read_only_fields = [
            'name',
            'image1',
            'price',
            'country',
            'description',
            'number_of_elements',
            'added_at',
            'content_type_display'
        ]

    def get_content_type_display(self, obj):
        return obj.content_type.model if obj.content_type else None

    def create(self, validated_data):
        user = self.context['request'].user
        model_name = validated_data.pop('content_type').lower()
        object_id = validated_data['object_id']

        try:
            content_type = ContentType.objects.get(model=model_name)
        except ContentType.DoesNotExist:
            raise serializers.ValidationError({
                'content_type': f"Model '{model_name}' not found."
            })

        try:
            product = content_type.get_object_for_this_type(id=object_id)
        except Exception:
            raise serializers.ValidationError({
                'object_id': f"Object with id '{object_id}' not found."
            })

        image = ''

        if getattr(product, 'image1', None):
            try:
                # Для ImageField
                image = product.image1.url
            except AttributeError:
                # Для URLField / CharField
                image = str(product.image1)

        elif getattr(product, 'photos', None):
            image = str(product.photos).split("|")[0]

        favorite, created = Favorite.objects.get_or_create(
            user=user,
            content_type=content_type,
            object_id=object_id,
            defaults={
                'name': str(getattr(product, 'name', '')),
                'image1': image,
                'price': float(getattr(product, 'price', 0) or 0),
                'country': str(getattr(product, 'country', '')),
                'description': str(getattr(product, 'description', '')),
                'number_of_elements': int(
                    getattr(product, 'number_of_elements', 1) or 1
                ),
            }
        )

        return favorite





class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

    def get_product(self, obj):
        return {
            'id': obj.product.id,
            'name': str(getattr(obj.product, 'name', '')),
            'price': float(getattr(obj.product, 'price', 0.0)),
        }


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'created_at', 'status', 'payment_receipt_url',
            'first_name', 'last_name', 'patronymic', 'phone', 'email', 'comment',
            'delivery_method', 'delivery_address', 'payment_method', 'total_price',
            'items'
        ]
