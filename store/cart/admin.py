from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'total', 'freight', 'status']
    list_display_links = ['pk', 'user', ]
    list_per_page = 50


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cart', 'product', 'unitary_value', 'quantity', ]
    list_display_links = ['pk', 'cart', 'product', ]
    list_per_page = 50


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
