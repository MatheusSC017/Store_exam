from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from pathlib import Path
from product.models import Product as ProductModel


class ProductSetupTestCase(APITestCase):
    def setUp(self) -> None:
        image = SimpleUploadedFile(name='test_image.jpg',
                                   content=open(settings.BASE_DIR / 'product/tests/image_test.png', 'rb').read(),
                                   content_type='image/jpeg')

        self.product = ProductModel.objects.create(
            name='Call of Duty WW III',
            price=300.0,
            score=4.9,
            image=image
        )
