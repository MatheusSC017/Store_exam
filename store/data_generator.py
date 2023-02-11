import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from pathlib import Path
from product.models import Product as ProductModel
from django.contrib.auth.models import User

with open('products.json') as f:
    data = json.load(f)

for product in data:
    image = SimpleUploadedFile(name='test_image.jpg',
                               content=open(settings.BASE_DIR / 'assets' / product['image'], 'rb').read(),
                               content_type='image/jpeg')

    ProductModel.objects.create(
        name=product['name'],
        price=product['price'],
        score=product['score'],
        image=image
    )

User.objects.create_user(
    username='UserTest',
    password='UserTest',
    email='user@user.com'
)
