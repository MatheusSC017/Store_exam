from cart.tests.setup import CartSetupTestCase
from cart.serializers import CartItemSerializer, CartWithItemsSerializer, CartSerializer
from collections import OrderedDict


class CartItemSerializerTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(CartItemSerializerTestCase, self).setUp()
        self.serializer = CartItemSerializer(self.cartitem)

    def test_serializer_fields(self) -> None:
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'cart', 'product', 'unitary_value', 'quantity'})

    def test_contents_of_serializer_fields(self) -> None:
        data = self.serializer.data
        self.assertEqual(data['cart'], self.cartitem.cart.pk)
        self.assertEqual(data['product'], self.cartitem.product.pk)
        self.assertEqual(data['unitary_value'], self.cartitem.unitary_value)
        self.assertEqual(data['quantity'], self.cartitem.quantity)


class CartWithItemsSerializerTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(CartWithItemsSerializerTestCase, self).setUp()
        self.serializer = CartWithItemsSerializer(self.cart)

    def test_serializer_fields(self) -> None:
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'user', 'total', 'freight', 'status', 'cartitem_set'})

    def test_contents_of_serializer_fields(self) -> None:
        data = self.serializer.data
        self.assertEqual(data['user'], self.cart.user.pk)
        self.assertEqual(data['total'], self.cart.total)
        self.assertEqual(data['freight'], self.cart.freight)
        self.assertEqual(data['status'], self.cart.status)
        self.assertEqual(data['cartitem_set'][0]['id'], self.cart.cartitem_set.all()[0].id)


class CartSerializerTestCase(CartSetupTestCase):
    def setUp(self) -> None:
        super(CartSerializerTestCase, self).setUp()
        self.serializer = CartSerializer(self.cart)

    def test_serializer_fields(self) -> None:
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'user', 'total', 'freight', 'status'})

    def test_contents_of_serializer_fields(self) -> None:
        data = self.serializer.data
        self.assertEqual(data['user'], self.cart.user.pk)
        self.assertEqual(data['total'], self.cart.total)
        self.assertEqual(data['freight'], self.cart.freight)
        self.assertEqual(data['status'], self.cart.status)
