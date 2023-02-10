from rest_framework import views, parsers, status
from rest_framework.response import Response
from product.models import Product as ProductModel
from .models import Cart as CartModel


class RegisterCartItem(views.APIView):
    parser_classes = [parsers.MultiPartParser, ]

    def post(self, request, format=None):
        # Get the current cart, otherwise create a new cart for the user
        cart = CartModel.objects.filter(user=request.user, status='Waiting')
        if not cart:
            cart = CartModel.objects.create(user=request.user)

        product = request.POST.get('product')
        quantity = request.POST.get('quantity')

        if product and quantity:
            # Check if the item was in the cart, if so add the new quantity, otherwise create a new item
            cart_item = cart.cartitem_set.filter(product=product)
            if cart_item:
                cart_item.quantity += quantity
            else:
                product_item = ProductModel.objects.get(pk=product)
                cart.cartitem_set.create(product=product_item,
                                         quantity=quantity,
                                         unitary_value=product_item.price)
        else:
            return Response('Both "product" and "quantity" are required.', status=status.HTTP_400_BAD_REQUEST)

        return Response(None, status.HTTP_202_ACCEPTED)


class RemoveCartItem(views.APIView):
    parser_classes = [parsers.MultiPartParser, ]

    def post(self, request, format=None):
        cart = Cart.objects.filter(user=request.user, status='Waiting')
        if not cart:
            return Response('Cart not found.', status=status.HTTP_400_BAD_REQUEST)

        product = request.POST.get('product')
        quantity = request.POST.get('quantity')

        if product and quantity:
            # Check if the item was in the cart, if so remove the requested quantity, otherwise do nothing
            cart_item = cart.cartitem_set.filter(product=product)
            if cart_item:
                # If all quantity removed then delete item from cart otherwise reduce quantity value
                if cart_item.quantity <= quantity:
                    cart_item.delete()
                else:
                    cart_item.quantity -= quantity
        else:
            return Response('Both "product" and "quantity" are required.', status=status.HTTP_400_BAD_REQUEST)

        return Response(None, status.HTTP_202_ACCEPTED)
