from cart.tests.setup import CartSetupTestCase
from rest_framework import status
from django.urls import reverse
from cart.models import Cart as CartModel, CartItem as CartItemModel


class MyCartViewTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(MyCartViewTestCase, self).setUp()
        self.view_url = reverse('MyCart')

    def test_request_to_my_cart_logged_out(self) -> None:
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_to_my_cart_logged_in(self) -> None:
        self.client.force_login(self.user)
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MyOrdersViewSetTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(MyOrdersViewSetTestCase, self).setUp()
        self.cart.status = 'F'
        self.cart.save()

        self.list_url = reverse('MyOrders-list')
        self.detail_url = reverse('MyOrders-detail', kwargs={'pk': self.cart.pk})

    def test_request_to_my_orders_list_logged_out(self) -> None:
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_to_my_orders_list_logged_in(self) -> None:
        self.client.force_login(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_to_my_orders_detail_logged_out(self) -> None:
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_to_my_orders_detail_logged_int(self) -> None:
        self.client.force_login(self.user)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CheckoutViewTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(CheckoutViewTestCase, self).setUp()
        self.view_url = reverse('Checkout')

    def test_request_to_checkout_logged_out(self) -> None:
        response = self.client.post(self.view_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_to_checkout_logged_in(self) -> None:
        self.client.force_login(self.user)
        response = self.client.post(self.view_url)
        # Check if the status has been updated
        cart = CartModel.objects.get(pk=self.cart.pk)
        self.assertEqual(cart.status, 'F')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RegisterCartItemViewTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(RegisterCartItemViewTestCase, self).setUp()
        self.view_url = reverse('RegisterCartItem')

    def test_request_to_register_new_cart_item_logged_out(self) -> None:
        response = self.client.post(self.view_url, data={'product': self.product.pk, 'quantity': 2})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_to_update_cart_item_logged_in(self) -> None:
        self.client.force_login(self.user)
        response = self.client.post(self.view_url, data={'product': self.product.pk, 'quantity': 2})

        # Check if the quantity in cart item has been updated
        cartitem = CartItemModel.objects.get(pk=self.cartitem.pk)
        self.assertEqual(cartitem.quantity, 5)

        # Make sure your cart's total amount and freight has been updated
        cart = CartModel.objects.get(pk=self.cart.pk)
        self.assertEqual(cart.total, 1000.0)
        self.assertEqual(cart.freight, 50.0)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_to_add_new_cart_item_logged_in(self) -> None:
        self.client.force_login(self.user)
        response = self.client.post(self.view_url, data={'product': self.product_2.pk, 'quantity': 2})

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
        self.view_url = reverse('RemoveCartItem')

    def test_request_to_remove_cart_item_logged_out(self) -> None:
        response = self.client.post(self.view_url, data={'product': self.product.pk, 'quantity': 2})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_to_update_cart_item_logged_in(self) -> None:
        self.client.force_login(self.user)
        response = self.client.post(self.view_url, data={'product': self.product.pk, 'quantity': 2})

        # Check if the quantity in cart item has been updated
        cartitem = CartItemModel.objects.get(pk=self.cartitem.pk)
        self.assertEqual(cartitem.quantity, 1)

        # Make sure your cart's total amount and freight has been updated
        cart = CartModel.objects.get(pk=self.cart.pk)
        self.assertEqual(cart.total, 200.0)
        self.assertEqual(cart.freight, 10.0)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_to_remove_cart_item_logged_in(self) -> None:
        self.client.force_login(self.user)
        response = self.client.post(self.view_url, data={'product': self.product.pk, 'quantity': 3})

        # Make sure your cart's total amount and freight has been updated
        cart = CartModel.objects.get(pk=self.cart.pk)
        self.assertEqual(cart.total, 0.0)
        self.assertEqual(cart.freight, 0.0)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
