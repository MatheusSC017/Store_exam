"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from cart.views import RegisterCartItem, RemoveCartItem, MyCart, Checkout
from product.views import ProductViewSet
from user.views import LoginView

router_root = DefaultRouter()
router_root.register('produtos', ProductViewSet, 'products')

urlpatterns = [
    path('', include(router_root.urls)),
    path('login/', LoginView.as_view()),
    path('carrinho/', MyCart.as_view()),
    path('carrinho/adicionar/', RegisterCartItem.as_view()),
    path('carrinho/remover/', RemoveCartItem.as_view()),
    path('carrinho/checkout/', Checkout.as_view()),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
