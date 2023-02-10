from rest_framework.serializers import ModelSerializer
from .models import Cart, CartItem


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(ModelSerializer):
    cartitem_set = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['total', 'subtotal', 'freight', 'cartitem_set']
