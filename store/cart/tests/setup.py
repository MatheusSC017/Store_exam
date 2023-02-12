from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from pathlib import Path
from django.contrib.auth.models import User
from cart.models import Cart as CartModel, CartItem as CartItemModel
from product.models import Product as ProductModel
from rest_framework.authtoken.models import Token


class CartSetupTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='UserTest',
            password='UserTest',
            email='user@user.com'
        )

        self.token = Token.objects.get_or_create(user=self.user)[0].key


        image = SimpleUploadedFile(name='test_image.jpg',
                                   content=open(settings.BASE_DIR / 'product/tests/image_test.png', 'rb').read(),
                                   content_type='image/jpeg')

        self.product = ProductModel.objects.create(
            name='Call of Duty WW III',
            price=200.0,
            score=4.9,
            image=image
        )

        self.product_2 = ProductModel.objects.create(
            name='Call of Duty Warzone',
            price=400.0,
            score=4.7,
            image=image
        )

        self.cart = CartModel.objects.create(user=self.user)

        self.cartitem = CartItemModel.objects.create(
            cart=self.cart,
            product=self.product,
            unitary_value=self.product.price,
            quantity=3
        )
