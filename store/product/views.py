from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    http_method_names = ['get', ]

    def get_queryset(self):
        qs = Product.objects.all()
        return qs

