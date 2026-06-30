from rest_framework import serializers
from .models import ShowerAssembly

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowerAssembly
        fields = '__all__' 
        read_only_fields = ('created_at', 'updated_at')

class ProductDetailSerializer(ProductSerializer):
    """
    Сериализатор для детального просмотра одного товара.
    Здесь можно переопределить поля или добавить дополнительные методы.
    """
    # Например, можно добавить поле с полной информацией о наличии
    stock_info = serializers.SerializerMethodField()

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields  # добавляем новое поле

    def get_stock_info(self, obj):
        if obj.stock:
            return f"Остаток: {obj.stock} шт."
        return "Нет в наличии"