from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through=ProductOrder)
    submitted = models.DateTimeField()
    po = models.CharField(blank=True, null=True, max_length=200)
    notes = models.TextField(blank=True, null=True)
    taken = models.ForeignKey(User, related_name='to_fill', on_delete=models.CASCADE, blank=True, null=True)
    filled = models.ForeignKey(User, related_name='filled', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.email
