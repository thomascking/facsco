from django.contrib import admin

from products.models import ProductGroup, Product


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_number', 'name', ]
