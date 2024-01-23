from django.core.management.base import BaseCommand

from tasks_2.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Orders data:'))
        products = Product.objects.all()

        for product in products:
            self.stdout.write(f'{self.style.ERROR(product.pk)}: {product}')

