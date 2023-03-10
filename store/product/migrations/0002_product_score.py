# Generated by Django 4.1.6 on 2023-02-10 00:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='score',
            field=models.FloatField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='avaliação'),
            preserve_default=False,
        ),
    ]
