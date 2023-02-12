from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.permissions import AllowAny
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny, ]
    http_method_names = ['get', ]
    order_fields = ['name', 'price', 'score', '-name', '-price', '-score', ]

    def get_queryset(self):
        qs = Product.objects.all()

        order_by = self.request.query_params.get('order_by')
        if order_by in self.order_fields:
            qs = qs.order_by(order_by)

        return qs
