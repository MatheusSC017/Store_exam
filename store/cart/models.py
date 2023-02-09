from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="usuário")
    total = models.FloatField(validators=[MinValueValidator(0)], verbose_name="total")
    subtotal = models.FloatField(validators=[MinValueValidator(0)], verbose_name="sub-total")
    freight = models.FloatField(verbose_name="frete")

    def __str__(self):
        return f'{self.user} - R$ {self.total:.2f}'

    class Meta:
        verbose_name = 'carrinho'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING, verbose_name="carrinho")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name="produto")
    unitary_value = models.FloatField(validators=[MinValueValidator(0)], verbose_name="valor unitário")
    quantity = models.PositiveSmallIntegerField(verbose_name="quantidade")

    def __str__(self):
        return f'{self.cart} - R$ {self.unitary_value * self.quantity:.2f}'

    class Meta:
        verbose_name = 'item do carrinho'
