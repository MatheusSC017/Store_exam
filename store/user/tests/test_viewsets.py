from user.tests.setup import UserSetupTestCase
from rest_framework import status
from django.urls import reverse
import json


class LoginViewTestCase(UserSetupTestCase):
    def setUp(self) -> None:
        super(LoginViewTestCase, self).setUp()
        self.view_url = reverse('Login')

    def test_request_to_login(self) -> None:
        response = self.client.post(self.view_url,
                                   json.dumps({'username': 'UserTest', 'password': 'UserTest'}),
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
