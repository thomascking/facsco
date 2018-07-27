from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

from products.models import Product


class Pricing(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)


class Company(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=100, null=True)
    available_products = models.ManyToManyField(Product, through=Pricing)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.email
