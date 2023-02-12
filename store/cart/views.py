from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework import views, status
from rest_framework.response import Response
from product.models import Product as ProductModel
from .models import Cart as CartModel, CartItem as CartItemModel
from .serializers import CartWithItemsSerializer, CartSerializer


class MyCart(views.APIView):
    def get(self, request, format=None):
        try:
            cart = CartModel.objects.get(user=request.user, status='W')
            return Response(data=CartWithItemsSerializer(cart).data, status=status.HTTP_200_OK)
        except CartModel.DoesNotExist:
            return Response('When choosing a product it will appear here.', status=status.HTTP_200_OK)


class MyOrders(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    http_method_names = ['get', ]

    def get_serializer_class(self, *args, **kwargs):
        if self.kwargs.get('pk'):
            return CartWithItemsSerializer
        else:
            return CartSerializer

    def get_queryset(self):
        qs = CartModel.objects.filter(user=self.request.user, status='F')
        return qs


class Checkout(views.APIView):
    def post(self, request, format=None):
        try:
            cart = CartModel.objects.get(user=request.user, status='W')
        except CartModel.DoesNotExist:
            return Response('Cart not found.', status.HTTP_400_BAD_REQUEST)

        cart.status = 'F'
        cart.save()

        return Response(None, status=status.HTTP_200_OK)


class RegisterCartItem(views.APIView):
    def post(self, request, format=None):
        # Get the current cart, otherwise create a new cart for the user
        try:
            cart = CartModel.objects.get(user=request.user, status='W')
        except CartModel.DoesNotExist:
            cart = CartModel.objects.create(user=request.user)

        product = request.data.get('product')
        quantity = int(request.data.get('quantity'))

        if product and quantity:
            # Check if the item was in the cart, if so add the new quantity, otherwise create a new item
            try:
                cart_item = cart.cartitem_set.get(product=product)
                cart_item.quantity += quantity
                cart_item.save()
            except CartItemModel.DoesNotExist:
                product_item = ProductModel.objects.get(pk=product)
                cart.cartitem_set.create(product=product_item,
                                         quantity=quantity,
                                         unitary_value=product_item.price)
        else:
            return Response('Both "product" and "quantity" are required.', status=status.HTTP_400_BAD_REQUEST)

        return Response(None, status=status.HTTP_200_OK)


class RemoveCartItem(views.APIView):
    def post(self, request, format=None):
        try:
            cart = CartModel.objects.get(user=request.user, status='W')
        except CartModel.DoesNotExist:
            return Response('Cart not found.', status=status.HTTP_400_BAD_REQUEST)

        product = request.data.get('product')
        quantity = int(request.data.get('quantity'))

        if product and quantity:
            # Check if the item was in the cart, if so remove the requested quantity, otherwise do nothing
            try:
                cart_item = cart.cartitem_set.get(product=product)
                # If all quantity removed then delete item from cart otherwise reduce quantity value
                if cart_item.quantity <= quantity:
                    cart_item.delete()
                else:
                    cart_item.quantity -= quantity
                    cart_item.save()
            except CartItemModel.DoesNotExist:
                pass
        else:
            return Response('Both "product" and "quantity" are required.', status=status.HTTP_400_BAD_REQUEST)

        return Response(None, status=status.HTTP_200_OK)
