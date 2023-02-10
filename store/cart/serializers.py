from rest_framework.serializers import ModelSerializer
from .models import Cart as CartModel, CartItem as CartItemModel


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItemModel
        fields = '__all__'


class CartWithItemsSerializer(ModelSerializer):
    cartitem_set = CartItemSerializer(many=True)

    class Meta:
        model = CartModel
        fields = ['id', 'user', 'total', 'status', 'freight', 'cartitem_set']


class CartSerializer(ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'
