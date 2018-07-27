from django.db import models


class ProductGroup(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    product_number = models.CharField(max_length=200)
    group = models.ForeignKey(ProductGroup, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
