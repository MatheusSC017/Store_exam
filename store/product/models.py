from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from utils import utils


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="produto")
    describe = models.TextField(verbose_name="descrição")
    price = models.FloatField(validators=[MinValueValidator(0)], verbose_name="preço")
    stock = models.PositiveSmallIntegerField(verbose_name="estoque")
    score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="avaliação")
    image = models.ImageField(upload_to='products/', verbose_name='imagem')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        utils.resize_image(self.image, new_width=600)

    class Meta:
        verbose_name = 'produto'
