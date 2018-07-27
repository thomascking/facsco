from django.contrib import admin

from order.models import ProductOrder, Order


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'submitted', ]
