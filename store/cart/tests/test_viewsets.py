from cart.tests.setup import CartSetupTestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from django.urls import reverse
from cart.models import Cart as CartModel, CartItem as CartItemModel
from rest_framework.test import force_authenticate
from cart.views import RemoveCartItem, RegisterCartItem, Checkout, MyCart, MyOrders
import json


class MyCartViewTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(MyCartViewTestCase, self).setUp()
        self.factory = APIRequestFactory()
        self.view_url = reverse('MyCart')
        self.view = MyCart.as_view()

    def test_request_to_my_cart_logged_out(self) -> None:
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_to_my_cart_logged_in(self) -> None:
        request = self.factory.get(self.view_url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MyOrdersViewSetTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(MyOrdersViewSetTestCase, self).setUp()
        self.cart.status = 'F'
        self.cart.save()

        self.factory = APIRequestFactory()

        self.list_url = reverse('MyOrders-list')
        self.detail_url = reverse('MyOrders-detail', kwargs={'pk': self.cart.pk})
        self.list_view = MyOrders.as_view({'get': 'list'})
        self.detail_view = MyOrders.as_view({'get': 'retrieve'})

    def test_request_to_my_orders_list_logged_out(self) -> None:
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_to_my_orders_list_logged_in(self) -> None:
        request = self.factory.get(self.list_url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = self.list_view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_to_my_orders_detail_logged_out(self) -> None:
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_to_my_orders_detail_logged_in(self) -> None:
        request = self.factory.get(self.detail_url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = self.detail_view(request, pk=self.cart.pk)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CheckoutViewTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(CheckoutViewTestCase, self).setUp()
        self.factory = APIRequestFactory()
        self.view_url = reverse('Checkout')
        self.view = Checkout.as_view()

    def test_request_to_checkout_logged_out(self) -> None:
        response = self.client.post(self.view_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_to_checkout_logged_in(self) -> None:
        request = self.factory.post(self.view_url,
                                    HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = self.view(request)

        # Check if the status has been updated
        cart = CartModel.objects.get(pk=self.cart.pk)
        self.assertEqual(cart.status, 'F')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RegisterCartItemViewTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(RegisterCartItemViewTestCase, self).setUp()
        self.factory = APIRequestFactory()
        self.view_url = reverse('RegisterCartItem')
        self.view = RegisterCartItem.as_view()

    def test_request_to_register_new_cart_item_logged_out(self) -> None:
        response = self.client.post(self.view_url,
                                    json.dumps({'product': self.product.pk, 'quantity': 2}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_to_update_cart_item_logged_in(self) -> None:
        request = self.factory.post(self.view_url,
                                    json.dumps({'product': self.product.pk, 'quantity': 2}),
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the quantity in cart item has been updated
        cartitem = CartItemModel.objects.get(pk=self.cartitem.pk)
        self.assertEqual(cartitem.quantity, 5)

        # Make sure your cart's total amount and freight has been updated
        cart = CartModel.objects.get(pk=self.cart.pk)
        self.assertEqual(cart.total, 1000.0)
        self.assertEqual(cart.freight, 50.0)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_to_add_new_cart_item_logged_in(self) -> None:
        request = self.factory.post(self.view_url,
                                    json.dumps({'product': self.product_2.pk, 'quantity': 2}),
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the new cart item has been created
        cartitem = CartItemModel.objects.get(cart=self.cart.pk, product=self.product_2.pk)
        self.assertEqual(cartitem.quantity, 2)

        # Make sure your cart's total amount has been updated
        cart = CartModel.objects.get(pk=self.cart.pk)
        self.assertEqual(cart.total, 1400.0)
        # Shipping was maintained because the price is greater than or equal to 250
        self.assertEqual(cart.freight, 30.0)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RemoveCartItemViewTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(RemoveCartItemViewTestCase, self).setUp()
        self.factory = APIRequestFactory()
        self.view_url = reverse('RemoveCartItem')
        self.view = RemoveCartItem.as_view()

    def test_request_to_remove_cart_item_logged_out(self) -> None:
        response = self.client.post(self.view_url,
                                    json.dumps({'product': self.product.pk, 'quantity': 2}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_request_to_update_cart_item_logged_in(self) -> None:
        request = self.factory.post(self.view_url,
                                    json.dumps({'product': self.product.pk, 'quantity': 2}),
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the quantity in cart item has been updated
        cartitem = CartItemModel.objects.get(pk=self.cartitem.pk)
        self.assertEqual(cartitem.quantity, 1)

        # Make sure your cart's total amount and freight has been updated
        cart = CartModel.objects.get(pk=self.cart.pk)
        self.assertEqual(cart.total, 200.0)
        self.assertEqual(cart.freight, 10.0)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_to_remove_cart_item_logged_in(self) -> None:
        request = self.factory.post(self.view_url,
                                    json.dumps({'product': self.product.pk, 'quantity': 3}),
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION='Token {}'.format(self.token))
        force_authenticate(request, user=self.user)
        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Make sure your cart's total amount and freight has been updated
        cart = CartModel.objects.get(pk=self.cart.pk)
        self.assertEqual(cart.total, 0.0)
        self.assertEqual(cart.freight, 0.0)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
