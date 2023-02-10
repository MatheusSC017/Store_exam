# Generated by Django 4.1.6 on 2023-02-10 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('W', 'Esperando'), ('A', 'Abandonado'), ('F', 'Finalizado')], default='W', max_length=1, verbose_name='status'),
            preserve_default=False,
        ),
    ]
