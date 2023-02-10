from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'score', ]
    list_display_links = ['pk', 'name', ]
    search_fields = ['name', ]
    list_per_page = 50


admin.site.register(Product, ProductAdmin)
