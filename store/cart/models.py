from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from product.models import Product


class Cart(models.Model):
    STATUS = (
        ('W', 'Esperando'),
        ('A', 'Abandonado'),
        ('F', 'Finalizado'),
    )

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="usuário")
    total = models.FloatField(default=0, validators=[MinValueValidator(0)], verbose_name="total")
    freight = models.FloatField(default=0, verbose_name="frete")
    status = models.CharField(default='W', max_length=1, choices=STATUS, verbose_name='status')

    def __str__(self):
        return f'{self.user} - {self.status} - R$ {self.total:.2f}'

    class Meta:
        verbose_name = 'carrinho'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.DO_NOTHING, verbose_name="carrinho")
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name="produto")
    unitary_value = models.FloatField(validators=[MinValueValidator(0)], verbose_name="valor unitário")
    quantity = models.PositiveSmallIntegerField(verbose_name="quantidade")

    def __init__(self, *args, **kwargs):
        super(CartItem, self).__init__(*args, **kwargs)
        self.__original_quantity = self.quantity

    def __str__(self):
        return f'{self.cart} - R$ {self.unitary_value * self.quantity:.2f}'

    class Meta:
        verbose_name = 'item do carrinho'


def cart_update(instance, original_quantity):
    if instance.quantity != original_quantity:
        difference = int(original_quantity) - int(instance.quantity)

        instance.cart.total -= difference * instance.unitary_value
        if instance.unitary_value < 250.0:
            instance.cart.freight -= difference * 10
        instance.cart.save()


@receiver(post_save, sender=CartItem)
def cart_update_when_adding_or_updating_item(sender, instance, created, **kwargs):
    original_quantity = 0 if created else instance._CartItem__original_quantity
    cart_update(instance, original_quantity)


@receiver(post_delete, sender=CartItem)
def cart_update_when_deleting_item(sender, instance, **kwargs):
    original_quantity = instance.quantity
    instance.quantity = 0
    cart_update(instance, original_quantity)
