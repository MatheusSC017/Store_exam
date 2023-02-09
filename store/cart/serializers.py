from rest_framework.serializers import ModelSerializer
from .models import Cart, CartItem


class CartSerializer(ModelSerializer):
    class Model:
        model = Cart
        fields = '__all__'


class CartItemSerializer(ModelSerializer):
    class Model:
        model = CartItem
        fields = '__all__'
