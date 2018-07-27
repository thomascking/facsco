import csv

from django.core.management.base import BaseCommand, CommandError
from products.models import Product, ProductGroup
from usermanagement.models import Company


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('file_location', nargs='+', type=str)

    def handle(self, *args, **options):
        for file_location in options['file_location']:
            with open(file_location) as file:
                csv_reader = csv.DictReader(file, delimiter=',')
                for row in csv_reader:
                    self.stdout.write('Product ID: %s, Product Name: %s' % (row['item_id'], row['item_desc']))
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
                    customer.available_products.add(prod)

            self.stdout.write(self.style.SUCCESS('Successfully loaded file "%s"' % file_location))
