from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserSetupTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="UserTest",
            password="UserTest",
            email="user@user.com"
        )
