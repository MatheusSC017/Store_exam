from product.tests.setup import ProductSetupTestCase
from product.serializers import ProductSerializer


class ProductSerializerTestCase(ProductSetupTestCase):
    def setUp(self) -> None:
        super(ProductSerializerTestCase, self).setUp()
        self.serializer = ProductSerializer(self.product)

    def test_serializer_fields(self) -> None:
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'price', 'score', 'image'})

    def test_contents_of_serializer_fields(self) -> None:
        data = self.serializer.data
        self.assertEqual(data['name'], self.product.name)
        self.assertEqual(data['price'], self.product.price)
        self.assertEqual(data['score'], self.product.score)
