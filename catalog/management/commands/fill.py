from django.core.management import BaseCommand
import datetime
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        products = [
            {'product_name': 'rambutan', 'description': 'hairy red', 'image': '', 'category': '1', 'price': '2000',
             'creation_date': datetime.date.today(), 'date_of_update': datetime.date.today()},
            {'product_name': 'peaches', 'description': 'hairy orange', 'image': '', 'category': '1',
             'price': '300',
             'creation_date': datetime.date.today(), 'date_of_update': datetime.date.today()},
            {'product_name': 'cucumbers', 'description': 'long green', 'image': '', 'category': '2',
             'price': '180',
             'creation_date': datetime.date.today(), 'date_of_update': datetime.date.today()},
            {'product_name': 'tomatoes', 'description': 'round red', 'image': '', 'category': '2',
             'price': '260',
             'creation_date': datetime.date.today(), 'date_of_update': datetime.date.today()}
        ]
        categories = [
            {'category_name': 'fruits', 'description': 'lots of vitamins'},
            {'category_name': 'vegetables', 'description': 'veggies adore them'}
        ]

        products_list = []
        categories_list = []

        for item in products:
            products_list.append(Product(**item))

        for item in categories:
            categories_list.append(Category(**item))

        Product.objects.all().delete()
        Product.objects.bulk_create(products_list)

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_list)
