from product.tests.setup import ProductSetupTestCase
from rest_framework import status
from django.urls import reverse


class ProductViewSetTestCase(ProductSetupTestCase):
    def setUp(self) -> None:
        super(ProductViewSetTestCase, self).setUp()
        self.list_url = reverse('Product-list')

    def test_request_to_product_list(self) -> None:
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
