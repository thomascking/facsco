import csv

from django.shortcuts import render
from io import TextIOWrapper
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, ProductGroup
from usermanagement.models import Company, Pricing


class ListProducts(APIView):
    def get(self, request, format=None):
        groups = ProductGroup.objects.all()
        company = request.user.userprofile.group
        resp = []
        for group in groups:
            products = group.product_set.filter(company=company)
            if products:
                resp.append(
                    {
                        "group": group.name,
                        "products": [{"number": p.product_number, "name": p.name} for p in products],
                    }
                )
        return Response(resp)


def upload_products(request):
    if request.FILES:
        file = TextIOWrapper(request.FILES['file'].file, encoding='ascii')
        csv_reader = csv.DictReader(file, delimiter=',')
        for row in csv_reader:
            prod, created = Product.objects.get_or_create(product_number=row['item_id'], name=row['item_desc'])
            if created:
                group, created = ProductGroup.objects.get_or_create(number=row['prod_grp_id'])
                if created:
                    group.name = row['prod_grp_id']
                    group.save()
                prod.group = group
                prod.save()
            customer, created = Company.objects.get_or_create(number=row['customer_id'])
            if created:
                customer.name = row['customer_name']
                customer.save()
            Pricing.objects.create(company=customer, product=prod, price=row['base_unit_price'])
    return render(request, 'upload.html')