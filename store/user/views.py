from django.contrib.auth import login
from rest_framework import permissions, views, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from . import serializers


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token = Token.objects.get_or_create(user=user)[0].key
        return Response(data={"token": token}, status=status.HTTP_202_ACCEPTED)
