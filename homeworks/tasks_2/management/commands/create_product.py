from random import randint
from django.core.management.base import BaseCommand, CommandParser

from tasks_2.models import Product


class Command(BaseCommand):
    help = 'Create products'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('quantity', type=int, default=1, help='Number of products')

    def handle(self, *args, **kwargs) -> None:
        count = kwargs['quantity']

        for i in range(1, count + 1):
            product = Product(
                title=f'Product {i}',
                description=f'Description of product {i}',
                price=1000.00,
                quantity=randint(1, 10),
            )
            self.stdout.write(self.style.SUCCESS(f'Added new order: {product}'))
            product.save()
