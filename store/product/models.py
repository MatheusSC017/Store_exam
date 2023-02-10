from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="produto")
    describe = models.TextField(verbose_name="descrição")
    price = models.FloatField(validators=[MinValueValidator(0)], verbose_name="preço")
    stock = models.PositiveSmallIntegerField(verbose_name="estoque")
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="avaliação")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'produto'
