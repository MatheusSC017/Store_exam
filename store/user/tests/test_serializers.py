from user.tests.setup import UserSetupTestCase
from user.serializers import LoginSerializer


class LoginSerializerTestCase(UserSetupTestCase):
    def setUp(self) -> None:
        super(LoginSerializerTestCase, self).setUp()
        self.serializer = LoginSerializer(self.user)

    def test_serializer_fields(self) -> None:
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set())
